from redis.exceptions import ConnectionError
from fastapi import APIRouter, HTTPException
import logging
from ..services.cache import Cache

router = APIRouter()
cache_manager = Cache()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


@router.get("/{scan_id}", summary="Get the status of a scan")
async def get_status(scan_id: str):
    try:
        logger.info(f"get_status: Now getting value for {scan_id}.")
        return {'status': cache_manager.get_value(scan_id)}
    except ConnectionError as e:
        logger.error(f"get_status: Failed with exception {e}.")
        raise HTTPException(status_code=503, detail="Unable to retrieve status.")
