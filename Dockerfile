FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    wget \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Get wait-for-it.sh
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it.sh

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 5000

# CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "wsgi:app"]
CMD ["sh", "-c", "flask db upgrade && gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:$PORT wsgi:app"]