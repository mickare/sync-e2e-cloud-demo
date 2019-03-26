from quart import Quart

from cloudsync.master.rest.api_v1 import scope
from cloudsync.master.rest.api_v1 import user


class QuartServer(Quart):
    def __init__(self, *args, **kwargs):
        super(QuartServer, self).__init__(*args, **kwargs)



app = QuartServer()
user.user.register(app)
scope.scope.register(app)

app.run(port=8888)
