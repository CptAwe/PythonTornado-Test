from tornado.options import options
import tornado.ioloop
import tornado.web

from app import make_app
from logger import show
import settings


if __name__ == "__main__":

    app = make_app()
    app.listen(settings._PORT)
    show("Im' listening on %s"%(settings._PORT))
    tornado.ioloop.IOLoop.current().start()