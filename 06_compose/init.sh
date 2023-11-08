#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE demodb;
    CREATE USER demouser;
    ALTER USER demouser WITH PASSWORD 'demopwd';
    ALTER USER demouser WITH LOGIN;

    ALTER DATABASE demodb OWNER TO demouser;
EOSQL

psql -v ON_ERROR_STOP=1 --username demouser --dbname "demodb" <<-EOSQL
    CREATE TABLE IF NOT EXISTS data (
        id SERIAL,
        content TEXT,
        primary key (id)
    ) TABLESPACE pg_default;
EOSQL
