from unittest.mock import AsyncMock

import pytest
from starlette.testclient import TestClient

from app import main
from app.storage.memory_storage import MemoryStorage


@pytest.fixture
def app():
    app_ = main.create_app()
    app_.storage = MemoryStorage()
    return app_


@pytest.fixture
def client(app):
    return TestClient(app)


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_detect_nginx_get(client):
    resp = client.get('/api/detect/nginx')
    assert resp.status_code == 405


def test_detect_nginx_empty(client):
    resp = client.post('/api/detect/nginx')
    assert resp.status_code == 422


def test_detect_nginx_fail(mocker, client):
    mocker.patch(
        'app.cases.cases.find_nginx',
        AsyncMock(side_effect=RuntimeError)
    )

    payload = {
        'domains': ['example.com', 'blog.detectify.com']
    }

    resp = client.post('/api/detect/nginx', json=payload)
    assert resp.status_code == 404


def test_detect_nginx_success(mocker, client):
    mocker.patch(
        'app.cases.cases.find_nginx',
        AsyncMock(return_value={'blog.detectify.com': {'nginx': True}})
    )

    payload = {
        'domains': ['example.com', 'blod.detectify.com']
    }

    resp = client.post('/api/detect/nginx', json=payload)
    assert resp.status_code == 200
