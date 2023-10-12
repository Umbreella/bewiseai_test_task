# Bewise-ai (REST-API)

## Backend

![python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white&style=for-the-badge&)
![fastapi](https://img.shields.io/badge/fastapi-009688?logo=fastapi&logoColor=white&style=for-the-badge&)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy_+_alembic-d71f00?logo=sqlite&logoColor=white&style=for-the-badge&)
![poetry](https://img.shields.io/badge/poetry-60A5FA?logo=poetry&logoColor=white&style=for-the-badge&)

## Database

![postgresql](https://img.shields.io/badge/postgresql-4169E1?logo=postgresql&logoColor=white&style=for-the-badge&)

## Cloud & CI/CD

![docker](https://img.shields.io/badge/docker-2496ED?logo=docker&logoColor=white&style=for-the-badge&)
![githubactions](https://img.shields.io/badge/githubactions-2088FF?logo=githubactions&logoColor=white&style=for-the-badge&)

---

## Description

[Task Description](TaskDescription.pdf)

## Getting Started

### Environment variables

To run the application, you need to set all the environment variables:

* **[.env.fastapi](.env)**
  ``

## Docker

1. docker-compose.yaml

```yaml
version: "3"

services:
  postgres_14:
    image: postgres:14
    container_name: postgres_14
    ports:
      - 5432:5432
    environment:
      - POSTGRES_PASSWORD=postgres
    volumes:
      - postgres:/var/lib/postgresql/data

  bewiseai_test_task:
    image: umbreella/bewiseai_test_task:latest
    container_name: bewiseai_test_task
    ports:
      - 8000:8000
    environment:
      - APP_POSTGRES_USERNAME=postgres
      - APP_POSTGRES_PASSWORD=postgres
      - APP_POSTGRES_DB=postgres
      - APP_POSTGRES_HOST=postgres_14
      - APP_POSTGRES_PORT=5432
    depends_on:
      - postgres_14

volumes:
  postgres:
```

2. Docker-compose run

```commandline
docker-compose up -d
```

3. Open bash in container

```commandline
docker exec -it bewiseai_test_task bash
```

4. Run migrations

```commandline
alembic upgrade head
```

## Endpoints

* REST-API Docs

```
[your_ip_address]/api/docs
```

## Requests

```commandline
curl -X 'POST' \
  'http://localhost:8000/api/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 1
}'
```
