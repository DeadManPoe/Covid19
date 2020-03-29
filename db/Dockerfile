FROM postgres:12-alpine

ADD ./postgresql.conf /etc/postgres/postgres.conf
ADD ./init.sh /docker-entrypoint-initdb.d/init.sh
ADD ./init_schemas.sh /docker-entrypoint-initdb.d/init_schemas.sh

CMD ["postgres", "-c", "config_file=/etc/postgres/postgres.conf"]
