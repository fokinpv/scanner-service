from unittest.mock import Mock

import pytest

import pytest

from app.storage.models import Task
from app.storage.memory_storage import MemoryStorage


@pytest.mark.asyncio
async def test_add():
    storage = MemoryStorage()
    task = Task(("example.com"))
    await storage.add(task)
    assert task.id == 0


@pytest.mark.asyncio
async def test_add_add():
    storage = MemoryStorage()
    task = Task(("example.com"))
    await storage.add(task)
    assert task.id == 0

    with pytest.raises(RuntimeError):
        await storage.add(task)


@pytest.mark.asyncio
async def test_get_fail():
    storage = MemoryStorage()
    with pytest.raises(RuntimeError):
        await storage.get(1)


@pytest.mark.asyncio
async def test_add_then_get():
    storage = MemoryStorage()
    task = Task(("example.com"))
    await storage.add(task)
    assert task.id == 0

    new_task = await storage.get(0)

    assert new_task is task


@pytest.mark.asyncio
async def test_add_update_get():
    storage = MemoryStorage()
    task = Task(("example.com"))
    await storage.add(task)
    assert task.id == 0

    task.domains_info = [Mock(), Mock()]

    await storage.update(task)

    new_task = await storage.get(0)
    assert new_task.domains_info != []
