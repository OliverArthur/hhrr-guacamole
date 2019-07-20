#!/bin/bash
# setup.sh
# Setup script for Flask Boilerplate only for Mac machines. Look at docs for windows

set -o errexit  # exit on any errors
# wait until postgres is started
while ! pg_isready -h "localhost" -p "5432" > /dev/null 2> /dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"

createdb || true    # create init database - pass on error
psql -c "create user guacamole with password 'Test1234x';" || true     # pass on error
psql -c "ALTER USER guacamole WITH SUPERUSER;" || true

psql -c "create database guacamoledb owner guacamole encoding 'utf-8';"
psql -c "create database guacamoletest_db owner guacamole encoding 'utf-8';"

psql -c "GRANT ALL PRIVILEGES ON DATABASE guacamoledb TO guacamole;"
psql -c "GRANT ALL PRIVILEGES ON DATABASE guacamoletest_db TO guacamole;"

python manage.py recreate_db
