class Base:
    def __init__(self, client=None):
        self._client = client

    async def __call__(self, domain):
        return await self.detect(domain)

    def with_client(self, client):
        self._client = client
        return self

    async def detect(self, domain):
        raise NotImplementedError
