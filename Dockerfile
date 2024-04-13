FROM python:3.12-slim

USER root

RUN useradd -m -u 1000 user
WORKDIR /app
RUN chown -R user:user /app

# Install system dependencies required for Chromium and git
RUN apt-get update && \
    apt-get install -y chromium git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY --chown=user:user . /app
EXPOSE 8501

# Set the PATH for Chromium
ENV CHROMIUM_PATH /usr/bin/chromium

RUN chown -R user:user /app
USER user

CMD ["streamlit", "run", "app.py"]
