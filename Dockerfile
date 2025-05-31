FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock* ./

RUN pip install uv

RUN uv sync --frozen

COPY . .

EXPOSE 8080

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

CMD ["uv", "run", "python", "main.py"]
