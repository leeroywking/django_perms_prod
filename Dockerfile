FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
# ENTRYPOINT ["gunicorn"]
# CMD ["jwt_django.wsgi:application", "--bind", "0.0.0.0:8000", "--workers","4"]
