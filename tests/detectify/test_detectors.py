from unittest.mock import AsyncMock, Mock

import pytest

from app.detectify.detectors import Nginx
from app.detectify.models import Domain


@pytest.fixture
def client_nginx():
    _client = Mock()
    _client.head = AsyncMock(return_value=Mock(headers={'server': 'nginx'}))
    return _client


@pytest.fixture
def client_not_nginx():
    _client = Mock()
    _client.head = AsyncMock(return_value=Mock(headers={'server': 'server'}))
    return _client


@pytest.fixture
def domain():
    return Domain('example.com')


@pytest.mark.asyncio
async def test_nginx_success(client_nginx, domain):
    domain = await Nginx(client=client_nginx).for_domain(domain).detect()

    assert domain.name == 'example.com'
    assert domain.properties['nginx']


@pytest.mark.asyncio
async def test_nginx_failure(client_not_nginx, domain):
    domain = await Nginx(client=client_not_nginx).for_domain(domain).detect()

    assert domain.name == 'example.com'
    assert domain.properties['nginx'] is False
