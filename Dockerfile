FROM python:3.9

WORKDIR /code

COPY ./obyazatelno_k_ustanovke.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./website /code/website
COPY ./migrations /code/migrations
COPY ./main.py /code/
COPY ./alembic.ini /code/


CMD ["uvicorn","main:app","--host", "0.0.0.0","--port","80"]