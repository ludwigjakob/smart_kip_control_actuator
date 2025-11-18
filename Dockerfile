FROM python:3.11-slim

WORKDIR /app

# Installiere gcc und Python-Header für native Builds
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]