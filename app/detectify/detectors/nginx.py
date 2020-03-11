from .base import Base


class Nginx(Base):

    @staticmethod
    def is_nginx(resp):
        return resp.headers.get('server', '') == 'nginx'

    async def detect(self):
        url = f'http://{self._domain.name}'
        print(url)

        resp = await self._client.head(url)

        is_nginx = self.is_nginx(resp)

        self._domain.add_property(
            name='nginx',
            value=is_nginx
        )
        return self._domain
