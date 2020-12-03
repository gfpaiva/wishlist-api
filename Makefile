#!/bin/sh

install: 
	pip install -r app/requirements.txt

lint: 
	flake8 app/src

test: 
	pytest

test-cov: 
	pytest --cov-config=.coveragerc --cov=app --cov-report term --cov-report html
