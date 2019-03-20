from uuid import UUID

from quart import Blueprint

storage = Blueprint('storage', __name__)


@storage.route('/storage', methods=['GET'])
async def list_storages():
    pass


@storage.route('/storage/<uuid:storage_slug>', methods=['GET'])
async def get_storage(storage_slug: UUID):
    pass


@storage.route('/storage/<uuid:storage_slug>', methods=['PATCH'])
async def update_storage(storage_slug: UUID):
    pass


@storage.route('/storage/<uuid:storage_slug>', methods=['PUT'])
async def create_storage(storage_slug: UUID):
    pass


@storage.route('/storage/<uuid:storage_slug>', methods=['DELETE'])
async def delete_storage(storage_slug: UUID):
    pass

