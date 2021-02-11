"""
class for an individual websocket user
"""

class WsUser():
    id = None
    tag = None
    socketHandler = None

    def __init__(self):
        super().__init__()