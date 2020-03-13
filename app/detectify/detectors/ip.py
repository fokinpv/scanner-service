import socket

from .base import Base


class SocketClient:

    async def get_ip(self, domain):
        # FIXME Change to <asynchronous library
        return socket.gethostbyname(domain)


class IP(Base):

    async def detect(self, domain_info):
        ip_ = await self._client.get_ip(domain_info.name)

        domain_info.add_property(
            name='ip',
            value=ip_
        )
        return domain_info
