import logging

from fastapi import FastAPI

from app import api, config
from app.storage.memory_storage import MemoryStorage

log = logging.getLogger(__name__)   # pylint: disable=invalid-name


def create_app():
    app_ = FastAPI(  # pylint: disable=invalid-name
        title='Detectify Service',
        description='Detectify service',
        version="0.0.1",
    )
    app_.include_router(api.router)

    @app_.on_event("startup")
    def startup():
        app_.storage = MemoryStorage()


    return app_


app = create_app()
