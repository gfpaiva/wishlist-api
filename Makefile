#!/bin/sh

install: 
	pip install -r app/requirements.txt

lint: 
	flake8 app/src --count --show-source --statistics --max-line-length=90

test: 
	pytest

test-cov: 
	pytest --cov-config=.coveragerc --cov=app --cov-report term --cov-report html --cov-report=xml
