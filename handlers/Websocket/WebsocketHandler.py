from tornado.websocket import WebSocketHandler

class WSHandler(WebSocketHandler):
    clients = []

    def open(self):
        self.clients.append(self)
        print('new connection')
        self.write_message("Hello World")

    def on_message(self, message):
        print('message received %s' % message)

    def on_close(self):
        self.clients.remove(self)
        print('closed connection')
