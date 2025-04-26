#!/bin/sh

## Repeat command until port 5432 on address db is not ready.
until !</dev/tcp/db/5433
do
echo "Waiting for database connection for 5 seconds..."

## Wait for 5 seconds before check again.
sleep 5
done
echo "Database server ready..."
alembic upgrade head
python main.py
#### run your server afterwards