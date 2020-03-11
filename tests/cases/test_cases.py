import pytest

from app.storage.memory_storage import MemoryStorage
from app.cases.cases import find_nginx


@pytest.fixture
def storage():
    return MemoryStorage()


async def mock_detect_nginx(domains):
    for idx, domain in enumerate(domains):
        if idx % 2 == 0:
            domain.add_property(
                name='nginx',
                value=True
            )
        else:
            domain.add_property(
                name='nginx',
                value=False
            )
    return domains


@pytest.mark.asyncio
async def test_find_nginx(mocker, storage):
    mocker.patch('app.detectify.scripts.detect_nginx', mock_detect_nginx)
    domains = await find_nginx(storage, ('example.com', 'blog.detectify.com'))
    assert len(domains) == 1
