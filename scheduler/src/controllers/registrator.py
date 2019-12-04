from .health import HealthController

class Registrator:
    def __init__(self, app, base_url):
        self.controllers = [HealthController()]
        self.app = app
        self.base_url = base_url

    def register_controllers(self):
        for controller in self.controllers:
            controller.register_routes(self.app, self.base_url)