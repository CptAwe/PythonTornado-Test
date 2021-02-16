"""
A manager for handling messages between the 
server and the clients (admin/users)
"""

from modules.Users.user import WsUser
from modules.UsersManager import WsUserMng

class messagesMng():
    clients = None

    def __init__(self, _clients: WsUserMng):
        self.clients = _clients
        super().__init__()
    
    def sendMessage(self, recipients_tags : list, message):
        if type(recipients_tags) != list: recipients_tags = [recipients_tags]
        for tag in recipients_tags:
            print("___", tag)
            recipients = self.clients.clientsWith(tag)
            for rec in recipients:
                rec.socketHandler._sendMessage(message)
            # tag.socketHandler._sendMessage(message)
