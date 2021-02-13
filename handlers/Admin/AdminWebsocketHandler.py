from tornado.websocket import WebSocketHandler

import json

from modules.UsersManager import WsUserMng
from handlers.Admin.Admin import AdminMng
from modules.Messenger.messagesManager import messagesMng


class AdminWSHandler(WebSocketHandler):
    clientPool: WsUserMng = None
    messenger: messagesMng = None
    admin: AdminMng = None

    def __init__(self, application, request, **kwargs):
        self.clientPool = kwargs.pop("users")
        self.admin = AdminMng(self)
        self.messenger = messagesMng(self.admin)

        super().__init__(application, request, **kwargs)

    def open(self):
        self.write_message("Hello admin")
        print("The admin has connected")

    def on_message(self, message):
        message = json.loads(message)
        print('admin: %s' % (message))
        self.messenger.sendMessage(self.clientPool.clients, message["message"])

    def on_close(self):
        print('closed connection with admin')

