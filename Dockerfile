FROM python:3.6

RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev

ADD requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

ADD app /root/app
ENV PYTHONPATH=/root/app
WORKDIR /root/app

ENTRYPOINT ["python"]
CMD ["app.py"]
