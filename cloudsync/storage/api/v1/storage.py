from uuid import UUID

import quart
from quart import Blueprint, Request

request: Request = quart.request
storage = Blueprint('storage', __name__)


@storage.route('/storage/<uuid:scope>/prepare_upload/<str:token>', methods=['PUT'])
async def prepare_upload(scope: UUID, token: str):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>', methods=['PUT'])
async def create_scope(scope: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>', methods=['DELETE'])
async def delete_scope(scope: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>/file', methods=['GET'])
async def list_files(scope: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>/file/<uuid:file>', methods=['GET'])
async def get_file(scope: UUID, file: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>/file/<uuid:file>', methods=['PUT'])
async def upload_file(scope: UUID, file: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError


@storage.route('/storage/<uuid:scope>/file/<uuid:file>', methods=['DELETE'])
async def delete_file(scope: UUID, file: UUID):
    api_token = request.headers.get('API_TOKEN')
    raise NotImplementedError
