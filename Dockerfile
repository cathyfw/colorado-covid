FROM alpine

RUN adduser -D flaskuser

WORKDIR /home/flaskuser

COPY requirements.txt requirements.txt

# trying to fix problem with pandas and matplotlib  https://stackoverflow.com/questions/54890328/installing-pandas-in-docker-alpine
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk add build-base libzmq musl-dev python3 python3-dev zeromq-dev

RUN apk add make automake gcc g++ subversion python3-dev libzmq
RUN apk add --update --no-cache py3-numpy py3-pandas@testing

#RUN python -m venv venv
#RUN venv/bin/pip install cython
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install gunicorn

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY app app
#COPY migrations migrations
COPY flask_app.py boot.sh ./
#COPY flask_app.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP flask_app.py

RUN chown -R flaskuser:flaskuser ./
USER flaskuser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]