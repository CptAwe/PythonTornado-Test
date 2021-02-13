from tornado.websocket import WebSocketHandler

from handlers.Admin.Admin import AdminMng

class AdminWSHandler(WebSocketHandler):
    clientPool = None

    def __init__(self, application, request, **kwargs):
        self.clientPool = kwargs.pop("users")

        super().__init__(application, request, **kwargs)

    def open(self):
        self.write_message("Hello admin")
        print("The admin has connected")

    def on_message(self, message):
        print('admin: %s'%(message))

    def on_close(self):
        print('closed connection with admin')
