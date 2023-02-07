FROM python:3.8

RUN  apt update

RUN apt install net-tools \
        python3-psycopg2

RUN python3 -m pip install uvicorn \
        fastapi \
        sqlalchemy \
        psycopg2-binary

COPY ./src /usr/src

WORKDIR /usr/src/

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "172.16.238.2","--port", "6080"]