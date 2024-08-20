FROM postgres:16.4-alpine3.20
USER postgres

# Copy Postgres config file into container
#RUN mkdir /home/postgresql
COPY ./db/postgresql.conf /home/postgresql/postgresql.conf
COPY ./db/pg_hba.conf /home/postgresql/pg_hba.conf

# Override default Postgres config file
CMD ["postgres", "-c", "config_file=/home/postgresql/postgresql.conf", "-c", "hba_file=/home/postgresql/pg_hba.conf"]