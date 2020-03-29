FROM postgres:12-alpine

ADD ./postgresql.conf /etc/postgres/postgres.conf
ADD ./init.sh /docker-entrypoint-initdb.d/init.sh

CMD ["postgres", "-c", "config_file=/etc/postgres/postgres.conf"]
