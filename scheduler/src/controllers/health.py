from aiohttp import web


class HealthController:
    def __init__(self):
        self.resource = "/health"

    def register_routes(self, app: web.Application, base_url: str):
        app.router.add_get(base_url + self.resource, self.__health_)

    async def __health_(self, request: web.Request):
        print("received health request")
        return web.Response(text="OK")
