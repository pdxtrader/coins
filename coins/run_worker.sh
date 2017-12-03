# !/bin/bash

celery -A src.celery worker --loglevel=info