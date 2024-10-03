#!/bin/sh

## Repeat command until port 5432 on address db is not ready.
until nc -z -v -w30 db 5432
do
echo "Waiting for database connection for 5 seconds..."

## Wait for 5 seconds before check again.
sleep 5
done
echo "Database server ready..."

#### run your server afterwards