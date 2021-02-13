"""
A manager for handling messages between the 
server and the clients (admin/users)
"""

from modules.Users.user import WsUser
# from 

class messagesMng():
    sender = None

    def __init__(self, _sender):
        self.sender = _sender
        super().__init__()
    
    def sendMessage(self, recipients : list, message):
        for rep in recipients:
            rep.socketHandler._sendMessage(message)
