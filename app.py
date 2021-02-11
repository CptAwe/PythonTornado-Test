from tornado.web import Application, StaticFileHandler

from handlers.Welcome.WelcomeHandler import Welcome
from handlers.Websocket.WebsocketHandler import WSHandler

from modules.UsersManager import WsUserMng

userPool = WsUserMng()

handlers = [
    (r"/", Welcome),
    (r"/start", WSHandler, {'users': userPool}),
    (r"/static/(.*)", StaticFileHandler, {"path" : "./handlers/Welcome"})
]

def make_app():
    return Application(
        handlers = handlers
    )