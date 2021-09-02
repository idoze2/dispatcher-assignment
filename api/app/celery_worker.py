from celery import Celery
from celery.app import task
from celery.utils.log import get_task_logger
from .config import app_config
from .services.cache import Cache
from .services.blackbox import BlackBox

celery = Celery("tasks", broker=app_config["rabbitmq_url"])
cache_manager = Cache()
logger = get_task_logger(__name__)


@celery.task
def scan_url(scan_id, url):
    logger.info(f"Now running BlackBox process on [{scan_id}], for url '{url}'.")
    cache_manager.set_running(scan_id)
    try:
        BlackBox.process(url)
    except Exception as e:
        logger.info(f"BlackBox [{scan_id}] caught an exception: {e}")
        cache_manager.set_error(scan_id)
        return {"status": "ERROR"}
    cache_manager.set_complete(scan_id)
    return {"status": "COMPLETE"}
