FROM python:3.13.3-alpine3.22 AS builder

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

COPY pyproject.toml uv.lock* ./

RUN pip install --no-cache-dir uv

RUN uv sync --frozen

FROM python:3.13.3-alpine3.22

WORKDIR /app

RUN apk add --no-cache \
    && rm -rf /var/cache/apk/*

COPY --from=builder /app/.venv /app/.venv

COPY main.py ./
COPY wsgi.py ./
COPY gunicorn.conf.py ./
COPY src ./src
COPY pyproject.toml ./
COPY uv.lock* ./

RUN rm -rf /root/.cache /usr/share/doc /usr/share/man /usr/share/locale \
    && find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true \
    && find . -name "*.pyc" -delete \
    && find . -name "*.pyo" -delete

EXPOSE 8080

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONOPTIMIZE=2
ENV FLASK_ENV=production
ENV PATH="/app/.venv/bin:$PATH"

CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
