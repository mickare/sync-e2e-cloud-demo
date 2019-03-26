from cloudsync.master.sync_master import SyncMaster


class MasterAPI:
    _instance: SyncMaster

    @staticmethod
    def instance() -> SyncMaster:
        return MasterAPI._instance
