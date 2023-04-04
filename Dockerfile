FROM python:3.11

RUN useadd -ms /bin/bash dev

USER dev

ENV PYTHONUNBUFEERED 1

WORKDIR /home/egi/api

ENV PATH $PATH:/home/egi/.local/bin

COPY requirements.txt /home/egi/api

RUN pip install -r requirements.txt

COPY . /home/egi/api
