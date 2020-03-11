import socket

import httpx


class HttpxClient:

    def __init__(self):
        self._client = httpx.AsyncClient()

    async def close(self):
        await self._client.aclose()

    async def head(self, url):
        return await self._client.head(url)

    async def get_ip(self, url):
        return socket.gethostbyname(url)
