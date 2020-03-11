class Base:
    def __init__(self, domain=None, client=None):
        self._domain = domain
        self._client = client

    async def __call__(self, domain):
        self._domain = domain
        return await self.detect()

    def for_domain(self, domain):
        self._domain = domain
        return self

    def with_client(self, client):
        self._client = client
        return self

    async def detect(self):
        raise NotImplementedError
