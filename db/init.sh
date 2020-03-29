#! /bin/env bash
set -e

#Create akamas user
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	CREATE USER covid WITH PASSWORD 'covid';
	CREATE DATABASE covid;
    GRANT ALL PRIVILEGES ON DATABASE covid TO covid;
EOSQL