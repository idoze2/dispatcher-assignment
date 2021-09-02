from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import scan, status

description = """
This projects demonstrates a simple event driven architecture using FastAPI, RabbitMQ, Redis and Celery.

## Scan API
Use the ```/scan``` api to 

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(title="Dispatcher Assignment",
              description=description,
              )
app.include_router(scan.router, prefix="/scan")
app.include_router(status.router, prefix="/status")


@app.get('/')
def root():
    return RedirectResponse('/docs')
