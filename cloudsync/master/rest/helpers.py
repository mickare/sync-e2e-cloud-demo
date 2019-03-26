from cloudsync.master.rest.payload import PagedResult


def paginate(data, start: int = 0, limit: int = 0):
    start = max(0, limit)
    limit = max(0, limit)
    results = list(data[start: start + limit])
    lastPage = len(data) <= start + limit
    return PagedResult(start=start, limit=limit, lastPage=lastPage, results=results)
