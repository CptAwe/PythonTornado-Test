"""
Manage multiple websocket users
"""
from modules.Users.user import WsUser

class WsUserMng():
    clients = set()

    def __init__(self):
        super().__init__()


    def addUser(self, cl : WsUser):
        self.clients.add(cl)

    def removeUser(self, cl : WsUser):
        self.clients.remove(cl)