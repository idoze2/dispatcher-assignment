import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = "REDIS_HOST"
REDIS_PORT = "REDIS_PORT"
RABBITMQ_URL = "RABBITMQ_URL"
CACHE_TTL = "CACHE_TTL"
RABBITMQ_USER = "RABBITMQ_USER"
RABBITMQ_PASS = "RABBITMQ_PASS"
RABBITMQ_HOST = "RABBITMQ_HOST"
RABBITMQ_PORT = "RABBITMQ_PORT"

app_config = {
    'redis_host': os.getenv(REDIS_HOST),
    'redis_port': os.getenv(REDIS_PORT),
    'rabbitmq_url': f'amqp://{os.getenv(RABBITMQ_USER)}:{os.getenv(RABBITMQ_PASS)}@{os.getenv(RABBITMQ_HOST)}:{os.getenv(RABBITMQ_PORT)}//',
    'cache_ttl': os.getenv(CACHE_TTL)
}
