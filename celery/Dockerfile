FROM python:2.7
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN groupadd -r celery && useradd -r -g celery celery
USER celery
CMD ["celery", "worker", "-l", "info"]
