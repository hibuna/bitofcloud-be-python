#!/bin/bash

# get password from docker secrets
DB_PASS=$(cat "/run/secrets/DB_PASS")

# create user for backend application
psql -c "CREATE USER \"${DB_USER}\" WITH PASSWORD '${DB_PASS}'"

# create databases
createdb --owner "${DB_USER}" "${DB_NAME}"
createdb --owner "${DB_USER}" "${DB_NAME}-test"