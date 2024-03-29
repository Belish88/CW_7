FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .