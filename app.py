from tornado.web import Application, StaticFileHandler

from settings import *

from handlers.Welcome.WelcomeHandler import Welcome
from handlers.Admin.ControlPanel.ControlPanelHandler import ControlPanel 
from handlers.Websocket.WebsocketHandler import WSHandler
from handlers.Admin.AdminWebsocketHandler import AdminWSHandler

from modules.Messenger.messagesManager import messagesMng
from modules.UsersManager import WsUserMng

userPool = WsUserMng()
Messenger = messagesMng(userPool)

handlers = [
    (r"/", Welcome),
    (r"/clientWS", WSHandler, {'users': userPool}),
    # (r"/adminWS", AdminWSHandler, {'users': userPool}),
    (r"/adminWS", AdminWSHandler),
    (r"/admin", ControlPanel, {'users': userPool}),
    (r"/static/(.*)", StaticFileHandler, {"path" : SETTINGS["static_path"]}),
]

def make_app():
    return Application(
        handlers,
        **SETTINGS
    )

def shutdown_app():
    '''
    Take a look at this:
    https://github.com/tornadoweb/tornado/issues/1791
    '''
    pass