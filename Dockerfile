# Dockerfile
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . /app

RUN uv pip install --system -r requirements.txt gunicorn

CMD ["sh", "-c", "uv run gunicorn --bind 0.0.0.0:${PORT:-8080} flaskdotcom.app:app"]
