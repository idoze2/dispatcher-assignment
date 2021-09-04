from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import scan, status

description = """
This API scans urls for known threats in an asynchronous manner.

## Scan API
Use ```/scan``` to enqueue a URL scan task and receive a scan_id for reference.

## Status API
Use ```/status/``` to retrieve the job status (accepted, running, etc.) of the scanning process.
"""

app = FastAPI(title="Dispatcher Assignment",
              description=description,
              )
app.include_router(scan.router, prefix="/scan")
app.include_router(status.router, prefix="/status")


@app.get('/')
def root():
    return RedirectResponse('/docs')
