from tornado.options import define

_PORT = 8888

def __apply_settings():

    opts = [
        ("port", _PORT),
    ]

    for sett in opts:
        define(*sett)

__apply_settings()