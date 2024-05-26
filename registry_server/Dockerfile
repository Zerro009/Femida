FROM python:3
ENV PYTHONBUFFERED 1

ADD . ./app
COPY ./requirements.txt /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "migrate", "--run-syncdb"]
