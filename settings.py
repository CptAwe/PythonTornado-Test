import os
from tornado.options import define

_PORT = 8888
SETTINGS = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    'debug' : True,
    'autoreload' : True,
    'compiled_template_cache' : False,
    'static_hash_cache' : False
}

def __apply_settings():

    opts = [
        ("port", _PORT),
    ]

    for sett in opts:
        define(*sett)

__apply_settings()