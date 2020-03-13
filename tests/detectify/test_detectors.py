from unittest.mock import AsyncMock, Mock

import pytest

from app.detectify.detectors import IP, Nginx
from app.detectify.models import Domain


@pytest.fixture
def client_ip():
    _client = Mock()
    _client.get_ip = AsyncMock(return_value='127.0.0.1')
    return _client


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
    domain = await Nginx(client=client_nginx).detect(domain)

    assert domain.name == 'example.com'
    assert domain.properties['nginx']


@pytest.mark.asyncio
async def test_nginx_failure(client_not_nginx, domain):
    domain = await Nginx(client=client_not_nginx).detect(domain)

    assert domain.name == 'example.com'
    assert domain.properties['nginx'] is False


@pytest.mark.asyncio
async def test_ip_success(client_ip, domain):
    domain = await IP(client=client_ip).detect(domain)

    assert domain.name == 'example.com'
    assert domain.properties['ip']  == '127.0.0.1'
