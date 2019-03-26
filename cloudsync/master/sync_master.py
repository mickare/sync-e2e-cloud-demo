import asyncio
from typing import Dict, Tuple, List
from uuid import UUID

from cloudsync.master.rest.payload import UpdateUploadPacket, FinishUploadPacket, ScopeModel, UpdateScopePacket


class Upload:

    def __init__(self, size: int):
        assert size > 0
        self._future = asyncio.Future()
        self.size = size
        self._progress = 0

    def update(self, packet: UpdateUploadPacket):
        if packet.bytes_progress:
            self._progress = packet.bytes_progress
            assert self._progress <= self.size

    def finish(self, packet: FinishUploadPacket):
        R = FinishUploadPacket.Result
        if packet.result == R.ERROR:
            self._future.set_exception(ValueError(packet.message))
        elif packet.result == R.CANCEL:
            self._future.cancel()
        elif packet.result == R.SUCCESS:
            total = packet.bytes_total
            if total == self.size:
                self._future.set_result(self)
            else:
                self._future.set_exception(ValueError("invalid size"))


class StorageSlave:
    _uploads: Dict[Tuple[UUID, str], Upload]

    def __init__(self, uuid: UUID):
        self.uuid = UUID
        self._uploads = dict()

    def get_upload(self, scope: UUID, token: str) -> Upload:
        return self._uploads.get((scope, token))


class Scope:
    def __init__(self, sid: UUID):
        self.sid = sid

    def serialize(self) -> ScopeModel:
        raise NotImplementedError

    def update(self, packet: UpdateScopePacket):
        raise NotImplementedError


class SyncMaster:

    def get_storage_slave_by_token(self, token: str) -> StorageSlave:
        raise NotImplementedError

    def get_storage_slave(self, slave: UUID) -> StorageSlave:
        raise NotImplementedError

    async def get_scopes(self) -> List[Scope]:
        raise NotImplementedError

    async def create_scope(self, owner: UUID) -> Scope:
        raise NotImplementedError

    async def get_scope(self, sid: UUID) -> Scope:
        raise NotImplementedError

    async def delete_scope(self, sid: UUID) -> Scope:
        raise NotImplementedError
