"""
The splash screen
"""

from tornado.web import RequestHandler

class ControlPanel(RequestHandler):
    def get(self):
        self.render("controlpanel.html")
