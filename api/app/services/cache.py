from uuid import uuid4

import redis

from ..config import app_config


class Cache:
    class Statuses:
        ACCEPTED = 'ACCEPTED'
        NOT_FOUND = 'NOT-FOUND'
        RUNNING = 'RUNNING'
        COMPLETE = 'COMPLETE'
        ERROR = 'ERROR'

    def __init__(self):
        self.redis_client = redis.Redis(host=app_config['redis_host'], port=app_config['redis_port'], db=0)

    def new(self):
        key = str(uuid4())[:8]  # Generates a unique 8-char scan_id
        self.redis_client.set(key, self.Statuses.ACCEPTED, ex=app_config['cache_ttl'])
        return key

    def get_value(self, key):
        value = self.redis_client.get(key)
        return value if value is not None else self.Statuses.NOT_FOUND

    def set_running(self, key):
        self.redis_client.set(key, self.Statuses.RUNNING, ex=app_config['cache_ttl'])

    def set_complete(self, key):
        self.redis_client.set(key, self.Statuses.COMPLETE, ex=app_config['cache_ttl'])

    def set_error(self, key):
        self.redis_client.set(key, self.Statuses.ERROR, ex=app_config['cache_ttl'])
