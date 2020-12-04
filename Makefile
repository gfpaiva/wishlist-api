#!/bin/sh

install: 
	pip install -r app/requirements.txt

dev: 
	docker-compose down
	docker-compose up -d

start: 
	PYTHON_ENV=${PYTHON_ENV} cd app && uvicorn src.infra.server:app --reload --port ${PORT}

dev-logs: 
	docker-compose logs -f

lint: 
	flake8 app/src --count --show-source --statistics --max-line-length=90

test: 
	pytest app/tests/services -s

test-cov: 
	pytest  app/tests/services --cov-config=.coveragerc --cov=app --cov-report term --cov-report html --cov-report=xml --ignore=app/tests/integration

test-integration: 
	docker-compose -f docker-compose.test.yaml down -v
	docker-compose  -f docker-compose.test.yaml up -d
	sleep 5
	PYTHON_ENV='test' DB_PASSWORD='wishlist' CACHE_PASSWORD='wishlist' pytest app/tests/integration -s
	docker-compose -f docker-compose.test.yaml down -v
