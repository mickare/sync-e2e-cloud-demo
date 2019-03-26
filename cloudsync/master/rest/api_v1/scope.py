from uuid import UUID

import quart
from quart import Blueprint, Request
from quart.exceptions import BadRequest, NotFound
from schematics.exceptions import DataError

from cloudsync.master.api import MasterAPI
from cloudsync.master.rest.helpers import paginate
from cloudsync.master.rest.payload import UpdateUploadPacket, FinishUploadPacket, ScopeModel, UpdateScopePacket

request: Request = quart.request

scope = Blueprint('scope', __name__)


def _get_slave_from_headers():
    auth: str = request.headers.get('Authorization', type=str)
    if auth.startswith('Bearer '):
        slave_token = auth[7:]
    else:
        raise NotFound()
    try:
        return MasterAPI.instance().get_storage_slave_by_token(slave_token)
    except:
        raise NotFound()


def _get_upload(sid: UUID, token: str):
    try:
        slave = _get_slave_from_headers()
        return slave.get_upload(sid, token)
    except KeyError:
        raise NotFound()


# Portal -> Master
@scope.route('/scope/<uuid:sid>/upload/<str:token>/status', methods=['PATCH'])
async def update_upload(sid: UUID, token: str):
    try:
        upload = _get_upload(sid, token)
        p = UpdateUploadPacket(await request.get_json())
        p.validate()
        upload.update(p)
    except DataError:
        raise BadRequest()


@scope.route('/scope/<uuid:sid>/upload/<str:token>', methods=['PUT'])
async def finish_upload(sid: UUID, token: str):
    try:
        upload = _get_upload(sid, token)
        p = FinishUploadPacket(await request.get_json())
        p.validate()
        upload.finish(p)
    except DataError:
        raise BadRequest()


# Storage rest
@scope.route('/scope', methods=['GET'])
async def list_scopes():
    start = request.args.get('start', 0, type=int)
    limit = request.args.get('limit', 1000, type=int)
    order = request.args.get('order', 'desc', type=str)
    master = MasterAPI.instance()
    scopes = await master.get_scopes()  # Bad, but this is a demo
    if order != 'desc':
        scopes = reversed(scopes)
    return paginate(scopes, start, limit).serialize()


@scope.route('/scope', methods=['PUT'])
async def create_scope():
    owner = request.args.get('owner', default=None, type=UUID)
    master = MasterAPI.instance()
    scope = await master.create_scope(owner=owner)
    return scope.serialize()


@scope.route('/scope/<uuid:sid>', methods=['GET'])
async def get_scope(sid: UUID):
    master = MasterAPI.instance()
    scope = await master.get_scope(sid)
    return scope.serialize()


@scope.route('/scope/<uuid:sid>', methods=['DELETE'])
async def delete_scope(sid: UUID):
    master = MasterAPI.instance()
    scope = await master.delete_scope(sid)
    return scope.serialize()


@scope.route('/scope/<uuid:sid>', methods=['PATCH'])
async def update_scope(sid: UUID):
    master = MasterAPI.instance()
    scope = await master.get_scope(sid)
    packet = UpdateScopePacket(await request.get_json())
    scope.update(packet)
    return scope.serialize()


# Index rest
@scope.route('/scope/<uuid:sid>/index', methods=['GET'])
async def get_index(sid: UUID):
    start = request.args.get('start', 0)
    limit = request.args.get('limit', 1000)
    raise NotImplementedError


# File rest
@scope.route('/scope/<uuid:sid>/file/<uuid:file_slug>', methods=['GET'])
async def get_file(sid: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:sid>/file/<uuid:file_slug>', methods=['PUT'])
async def put_file(sid: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:sid>/file/<uuid:file_slug>', methods=['PATCH'])
async def update_file(sid: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:sid>/file/<uuid:file_slug>', methods=['DELETE'])
async def delete_file(sid: UUID, file_slug: UUID):
    raise NotImplementedError
