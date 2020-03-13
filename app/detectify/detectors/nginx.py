import httpx

from .base import Base


class HttpxClient:

    def __init__(self):
        self._client = httpx.AsyncClient()

    async def close(self):
        await self._client.aclose()

    async def head(self, url):
        return await self._client.head(url)


class Nginx(Base):

    @staticmethod
    def is_nginx(resp):
        return resp.headers.get('server', '') == 'nginx'

    async def detect(self, domain):
        url = f'http://{domain.name}'

        resp = await self._client.head(url)

        is_nginx = self.is_nginx(resp)

        domain.add_property(
            name='nginx',
            value=is_nginx
        )
        return domain
