"""
The splash screen
"""

from tornado.web import RequestHandler

class Welcome(RequestHandler):
    def get(self):
        self.render("welcome.html")
