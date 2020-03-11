import logging

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.requests import Request
from pydantic import BaseModel

from app.cases import cases
from app.storage.abc_storage import Storage

log = logging.getLogger(__name__)   # pylint: disable=invalid-name
router = APIRouter()


def get_storage(request: Request):
    """Solver injector."""
    return request.app.storage


class DetectifyRequest(BaseModel):
    domains: list


class DetectifyResponse(BaseModel):
    domains: list


@router.post('/api/detect/nginx', response_model=DetectifyResponse)
async def detectify(
        request: DetectifyRequest,
        storage: Storage = Depends(get_storage)
):
    try:
        domains = await cases.find_nginx(storage, request.domains)
        print(domains)
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=404)
    else:
        return DetectifyResponse(domains=domains)
