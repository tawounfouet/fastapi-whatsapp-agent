FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY whatsapp_ai/ ./whatsapp_ai/
COPY main.py .

RUN pip install --upgrade pip && pip install --no-cache-dir .

COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN sed -i 's/\r//' /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]
