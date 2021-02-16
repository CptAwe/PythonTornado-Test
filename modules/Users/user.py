"""
class for an individual websocket user
"""
import random
from tornado.websocket import WebSocketHandler

class WsUser():
    id = None
    tag = None
    socketHandler = None

    __tagPool = ["well", "sum", "shadow", "article", "reconcile", "suspect", "pause", "screw", "patent", "loose"]

    def __init__(self, _id, wsHand: WebSocketHandler):
        self.id = _id
        self.tag = self.__generateTag()
        self.socketHandler = wsHand
        super().__init__()
    
    def __str__(self):
        return str({
            "id" : self.id,
            "tag" : self.tag,
            "WebSocket" : self.socketHandler
        })

    def __generateTag(self):
        # A cruede function to give tags
        return self.__tagPool[random.randint(0, len(self.__tagPool) - 1)]
