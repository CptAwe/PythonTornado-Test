import os

from tornado.web import Application, StaticFileHandler

from handlers.Welcome.WelcomeHandler import Welcome
from handlers.Admin.ControlPanel.ControlPanelHandler import ControlPanel 
from handlers.Websocket.WebsocketHandler import WSHandler
from handlers.Admin.AdminWebsocketHandler import AdminWSHandler

from modules.UsersManager import WsUserMng

userPool = WsUserMng()

settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
}

handlers = [
    (r"/", Welcome),
    (r"/clientWS", WSHandler, {'users': userPool}),
    (r"/adminWS", AdminWSHandler, {'users': userPool}),
    (r"/admin", ControlPanel),
    (r"/static/(.*)", StaticFileHandler, {"path" : settings["static_path"]}),
]

def make_app():
    return Application(
        handlers,
        **settings
    )