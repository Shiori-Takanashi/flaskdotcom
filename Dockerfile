FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . /app

CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8080", "flaskdotcom.app:app"]
