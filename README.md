# Url Scanning App Concept
This projects demonstrates a simple event driven architecture using FastAPI, RabbitMQ, Redis and Celery.

## Docker-Compose Run (Production) example
### Requirements

- Docker
  - [docker-compose](https://docs.docker.com/compose/install/)
  
1. Run command ```docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up``` to start up the RabbitMQ, Redis our application/worker instances.
2. Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API calls. You can monitor the execution of the celery tasks in the console logs or navigate to the RabbitMQ monitoring app: [http://localhost:15672](http://localhost:15672) (username: guest, password: guest).
3. Use the ```scale``` options to specify the amount of worker containers that are to be created. for example: ```docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up --scale worker=3``` to scale the application with more worker instances.

## Local Development Run example
### Requirements

- Python >= 3.7
  - [pip](https://pip.pypa.io/en/stable/installation/)
- RabbitMQ instance 
  - ```docker-compose up rabbitmq```
- Redis instance
  - ```docker-compose up redis```
- Local env values
  - ```cp api/app/sample.env api/app/.env```

### Install dependencies

Execute the following command: ```pip install -r api/requirements.txt```
### Run FastAPI app and Celery worker app

1. Start the FastAPI web application with ```uvicorn api.app.main:app --reload```.
2. Start the celery worker with ```celery -A api.app.celery_worker worker -l info```.
3. Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call.You can monitor the execution of the celery tasks in the console logs or navigate to the RabbitMQ monitoring app: [http://localhost:15672](http://localhost:15672) (username: guest, password: guest).