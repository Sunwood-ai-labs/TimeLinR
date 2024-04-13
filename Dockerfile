FROM python:3.12-slim

WORKDIR /app
USER root

# Install system dependencies required for Chromium and git
RUN apt-get update && \
    apt-get install -y chromium git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Set the PATH for Chromium
ENV CHROMIUM_PATH /usr/bin/chromium

CMD ["streamlit", "run", "app.py"]
