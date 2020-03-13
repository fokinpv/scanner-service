from .abc_storage import Storage


class MemoryStorage(Storage):

    def __init__(self):
        self._next_id = 0
        self._items = {}

    async def get(self, id_):
        if id_ not in self._items:
            raise RuntimeError
        return self._items[id_]

    async def get_list(self, limit):
        return [
            item
            for idx, item in enumerate(self._items.values())
            if idx < limit
        ]

    async def add(self, task):
        if task.id is not None:
            raise RuntimeError

        task.id = self._next_id
        self._items[task.id] = task
        self._next_id += 1

    async def update(self, task):
        if task.id is None:
            raise RuntimeError

        self._items[task.id] = task
