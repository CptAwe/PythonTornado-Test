from tornado.options import options
from tornado import autoreload
import tornado.ioloop
import tornado.web

from app import make_app
from modules.logger import show
import settings


if __name__ == "__main__":

    app = make_app()
    app.listen(settings._PORT)

    # enable auto reload
    autoreload.start()

    show("Im' listening on %s"%(settings._PORT))
    tornado.ioloop.IOLoop.current().start()