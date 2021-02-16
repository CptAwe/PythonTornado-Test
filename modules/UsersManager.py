"""
Manage multiple websocket users
"""
from modules.Users.user import WsUser

class WsUserMng():
    clients = set()

    def __init__(self):
        super().__init__()
    
    def __iter__(self):
        for cl in self.clients:
            yield cl

    def addUser(self, cl : WsUser):
        self.clients.add(cl)

    def removeUser(self, cl : WsUser):
        self.clients.remove(cl)
    
    def clientsWith(self, tag):
        # return all the clients with a specific tag
        clientsOfInterest = set()
        for cl in self.clients:
            if cl.tag == tag:
                clientsOfInterest.add(cl)
        
        return clientsOfInterest
    