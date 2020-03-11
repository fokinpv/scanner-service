from .base import Base


class IP(Base):

    async def detect(self, domain_info):
        ip_ = await self._client.get_ip(domain_info.name)

        domain_info.add_property(
            name='ip',
            value=ip_
        )
        return domain_info
