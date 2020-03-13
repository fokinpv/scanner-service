import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from pydantic import BaseModel

from app.cases import cases
from app.storage.abc_storage import Storage

log = logging.getLogger(__name__)   # pylint: disable=invalid-name
router = APIRouter()   # pylint: disable=invalid-name


def get_storage(request: Request):
    """Storage injector."""
    return request.app.storage


class GetDetectsResponse(BaseModel):
    tasks: List[dict]


class DetectifyRequest(BaseModel):
    domains: List[str]
    with_ip: Optional[bool]


class DetectifyResponse(BaseModel):
    domains: dict


@router.get('/', include_in_schema=False)
def index():
    return Response("I'm up", media_type='text/plain')


@router.get('/api/detects', response_model=GetDetectsResponse)
async def get_last_detects(
        limit: int = 10,
        storage: Storage = Depends(get_storage)
):
    try:
        tasks = await cases.get_last(storage, limit=limit)
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=404)
    else:
        return GetDetectsResponse(tasks=tasks)


@router.post('/api/detects', response_model=DetectifyResponse)
async def detectify(
        request: DetectifyRequest,
        storage: Storage = Depends(get_storage)
):
    try:
        domains = await cases.find_nginx(
            storage, request.domains, request.with_ip
        )
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=404)
    else:
        return DetectifyResponse(domains=domains)
