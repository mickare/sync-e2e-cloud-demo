from enum import Enum

from schematics import Model
from schematics.contrib.enum_type import EnumType
from schematics.types import *


class UpdateUploadPacket(Model):
    bytes_progress = IntType(min_value=0)


class FinishUploadPacket(Model):
    class Result(Enum):
        ERROR = -1
        SUCCESS = 0
        CANCEL = 1

    result = EnumType(Result, required=True)
    message = StringType()
    bytes_total = IntType(min_value=0)


class UpdateScopePacket(Model):
    owner: UUIDType()
    members: ListType(UUIDType)


class ScopeModel(Model):
    uuid: UUIDType(required=True)
    owner: UUIDType(required=True)
    members: ListType(UUIDType, required=True)
