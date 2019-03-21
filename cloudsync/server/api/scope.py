from uuid import UUID

import quart
from quart import Blueprint, Request

request: Request = quart.request

scope = Blueprint('scope', __name__)


# Storage api
@scope.route('/scope', methods=['GET'])
async def list_scopes():
    start = request.args.get('start', 0)
    limit = request.args.get('limit', 1000)
    raise NotImplementedError


@scope.route('/scope', methods=['PUT'])
async def create_scope():
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>', methods=['GET'])
async def get_scope(scope_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>', methods=['DELETE'])
async def delete_scope(scope_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>', methods=['PATCH'])
async def update_scope(scope_slug: UUID):
    raise NotImplementedError


# Index api
@scope.route('/scope/<uuid:scope_slug>/index', methods=['GET'])
async def get_index(scope_slug: UUID):
    start = request.args.get('start', 0)
    limit = request.args.get('limit', 1000)
    raise NotImplementedError


# File api
@scope.route('/scope/<uuid:scope_slug>/file/<uuid:file_slug>', methods=['GET'])
async def get_file(scope_slug: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>/file/<uuid:file_slug>', methods=['PUT'])
async def put_file(scope_slug: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>/file/<uuid:file_slug>', methods=['PATCH'])
async def update_file(scope_slug: UUID, file_slug: UUID):
    raise NotImplementedError


@scope.route('/scope/<uuid:scope_slug>/file/<uuid:file_slug>', methods=['DELETE'])
async def delete_file(scope_slug: UUID, file_slug: UUID):
    raise NotImplementedError
