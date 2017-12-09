from aiohttp import web
from routes import setup_routes


# All `aiohttp` server is built around `aiohttp.web.Application` instance.
# It is used for registering startup/cleanup signals, connecting routes etc.

app = web.Application()  # Create the application
setup_routes(app)
web.run_app(app, host="127.0.0.1", port=8000)
