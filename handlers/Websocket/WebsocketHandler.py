from tornado.websocket import WebSocketHandler
from modules.Users.user import WsUser
from modules.uuid import uuidManager

uuidMng = uuidManager()

class WSHandler(WebSocketHandler):
    clientPool = None
    user = WsUser()

    def __init__(self, application, request, **kwargs):
        self.clientPool = kwargs.pop("users")
        super().__init__(application, request, **kwargs)

    def open(self):
        self.user.id = uuidMng.generate()
        self.user.socketHandler = self
        self.clientPool.addUser(self.user)
        print('new connection <%s>'%self.user.id)
        self.write_message("Hello %s"%self.user.id)

    def on_message(self, message):
        print('%s: %s'%(self.user.id, message))

    def on_close(self):
        self.clientPool.removeUser(self.user)
        print('closed connection <%s>'%self.user.id)
