FROM python:3

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
COPY ./entrypoint /

RUN sed -i 's/\r$//g' /entrypoint

RUN chmod u+x /entrypoint

ENTRYPOINT ["/entrypoint"]

