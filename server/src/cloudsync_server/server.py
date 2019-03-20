from quart import Quart


class QuartServer(Quart):
    def __init__(self, *args, **kwargs):
        super(QuartServer, self).__init__(*args, **kwargs)
