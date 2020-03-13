from unittest.mock import AsyncMock, Mock

import pytest

from app.detectify import scripts, models


@pytest.fixture
def domains():
    return [models.Domain('example.com')]


@pytest.mark.asyncio
async def test_detect_nginx(mocker, domains):
    mocker.patch(
        'app.detectify.detectors.Nginx',
        Mock(return_value=AsyncMock())
    )
    domains_result = await scripts.detect_nginx(domains)
    assert domains_result


@pytest.mark.asyncio
async def test_detect_ip(mocker, domains):
    mocker.patch(
        'app.detectify.detectors.IP',
        Mock(return_value=AsyncMock())
    )
    domains_result = await scripts.detect_ip(domains)
    assert domains_result
