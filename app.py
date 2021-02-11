import os

from tornado.web import Application, StaticFileHandler

from handlers.Welcome.WelcomeHandler import Welcome
from handlers.Websocket.WebsocketHandler import WSHandler

handlers = [
    (r"/", Welcome),
    (r"/start", WSHandler),
    (r"/static/(.*)", StaticFileHandler, {"path" : "./handlers/Welcome"})
]

def make_app():
    return Application(
        handlers = handlers,
        # static_path=os.path.join(os.path.dirname(__file__), "static"),
        # template_path=os.path.join(os.path.dirname(__file__), "templates")
    )