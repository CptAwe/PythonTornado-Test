"""
Handles the admin abilities
"""
from tornado.websocket import WebSocketHandler

# TODO: Make only one admin login at any given time

class AdminMng():
    id = -1
    tag = "admin"
    socketHandler = None

    def __init__(self, scHand: WebSocketHandler):
        self.socketHandler = scHand
        super().__init__()

