import httpx


def get(url: str, **kwargs):
    response = httpx.get(url, **kwargs)
    return response


def post(url: str, **kwargs):
    response = httpx.post(url, **kwargs)
    return response


def put(url: str, **kwargs):
    response = httpx.put(url, **kwargs)
    return response


def delete(url: str, **kwargs):
    response = httpx.delete(url, **kwargs)
    return response
