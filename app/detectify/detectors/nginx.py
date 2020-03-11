from .base import Base


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
