"""
class for an individual websocket user
"""
from tornado.websocket import WebSocketHandler

class WsUser():
    id = None
    tag = None
    socketHandler = None

    def __init__(self, _id, wsHand: WebSocketHandler):
        self.id = _id
        self.tag = self.__generateTag()
        self.socketHandler = wsHand
        super().__init__()

    @staticmethod
    def __generateTag():
        # A cruede function to give tags
        return "random"
