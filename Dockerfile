FROM python:3.9-slim

WORKDIR /app

# Install necessary packages and clean up
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone your repository
RUN git clone https://github.com/phamofanthony/streamlit-portfolio.git .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the default port Streamlit uses
EXPOSE 8501

# Healthcheck to ensure the container is healthy
HEALTHCHECK CMD curl --fail http://localhost:${PORT:-8501}/healthz || exit 1

# Start the Streamlit application
ENTRYPOINT ["sh", "-c", "streamlit run 1_About_Me.py --server.port=${PORT:-8501} --server.address=0.0.0.0"]
