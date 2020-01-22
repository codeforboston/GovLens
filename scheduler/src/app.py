import logging
import os
import sys

import structlog
from aiohttp import web, ClientSession
from biz.scheduler import Scheduler
from controllers.registrator import Registrator


# close http client on server shutdown
async def __on_shutdown__(app):
    print("Server going down!")
    app["http_client"].close()


class Application:
    def __init__(self, config):
        self.base_url = "/api/GovLens/Scheduler/v1"
        self.log_format = (
            'Level="%(levelname)s", Date="%(asctime)s", ProcessId=%(process)d, '
            'Module="%(module)s", Logger="%(name)s", Method="%(funcName)s", Line=%(lineno)d, '
            "Message=%(message)s "
        )
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = config
        self.server = web.Application(client_max_size=1024 * 1024 * 10)  # max 10 MB
        self.server["http_client"] = ClientSession()
        self.server["server_base_url"] = self.base_url
        self.server["unauthenticated_urls"] = self.base_url + "/health"
        self.registrator = Registrator(self.server, self.base_url)
        self.__initialize_environ_vars__()
        self.__register_routes__()
        self.logger = self.__config_logger__()
        self.server.on_shutdown.append(__on_shutdown__)

    def __initialize_environ_vars__(self):
        for key, item in self.config.items():
            os.environ[key] = item

    def __register_routes__(self):
        self.registrator.register_controllers()

    def __config_logger__(self):
        logging.basicConfig(
            level=logging.INFO, format=self.log_format, stream=sys.stdout,
        )

        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.JSONRenderer(),
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
        )
        return structlog.get_logger("Startup")

    def run(self):
        self.logger.info("Starting service on 10004")
        self.start_scheduler()
        web.run_app(self.server, host="0.0.0.0", port=10004, access_log=None)

    def start_scheduler(self):
        scheduler_instance = Scheduler()
        scheduler_instance.read_settings()
        scheduler_instance.scrape_websites()
