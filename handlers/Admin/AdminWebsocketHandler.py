from tornado.websocket import WebSocketHandler
# from modules.Users.user import WsUser
# from modules.uuid import uuidManager

# uuidMng = uuidManager()

class AdminWSHandler(WebSocketHandler):
    clientPool = None

    def __init__(self, application, request, **kwargs):
        self.clientPool = kwargs.pop("users")
        super().__init__(application, request, **kwargs)

    def open(self):
        print("An admin has connected")

    def on_message(self, message):
        print('admin: %s'%(message))

    def on_close(self):
        self.clientPool.removeUser(self.user)
        print('closed connection with admin')
