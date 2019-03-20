from quart import Blueprint, session

user = Blueprint('user', __name__)


@user.route('/login', methods=['Post'])
async def login():
    session['logged_in'] = True


@user.route('/logout')
async def logout():
    session.pop('logged_in', None)
    return None
