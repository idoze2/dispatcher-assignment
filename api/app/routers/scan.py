from fastapi import APIRouter, HTTPException
from redis.exceptions import ConnectionError
from ..models.models import Url
from ..services.cache import Cache
from ..celery_worker import scan_url

router = APIRouter()
cache_manager = Cache()


@router.post("/", summary="Create a new Scan")
async def create_scan(url: Url):
    try:
        scan_id = cache_manager.new()  # create a new scan_id and create an entry in redis
        scan_url.delay(scan_id, url.url)  # enqueue scan task to RabbitMQ
        return {"scan_id": scan_id}
    except ConnectionError:
        raise HTTPException(status_code=503, detail=f"Unable to create scan for {url.url}")
