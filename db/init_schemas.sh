#! /bin/env bash

set -e

psql -v ON_ERROR_STOP=1 --username covid <<-EOSQL
    create table if not exists deaths (
        place varchar,
        latitude varchar not null,
        longitude varchar not null,
        timestamp timestamp not null,
        count bigint not null,
        created_at timestamp default current_timestamp,
        primary key (place, timestamp)
    );
EOSQL
