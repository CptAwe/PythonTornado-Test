"""
The splash screen
"""

from tornado.web import RequestHandler

from modules.UsersManager import WsUserMng

class ControlPanel(RequestHandler):
    
    clientPool : WsUserMng = None

    def __init__(self, application, request, **kwargs):
        self.clientPool = kwargs.pop("users")
        super().__init__(application, request, **kwargs)

    def get(self):

        _tags = set()
        for cl in self.clientPool:
            _tags.add(cl.tag)

        self.render("controlpanel.html", tags = _tags)
