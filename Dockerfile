FROM python:3.13.3-alpine3.22

WORKDIR /app

RUN apk add --no-cache \
    ffmpeg \
    curl \
    && rm -rf /var/cache/apk/*

COPY pyproject.toml uv.lock* ./

RUN pip install uv

RUN uv sync --frozen

COPY . .

EXPOSE 8080

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONOPTIMIZE=2
ENV FLASK_ENV=production

CMD ["uv", "run", "gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
