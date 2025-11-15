# Start from a base image
FROM python:3.11.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libgomp1 gcc g++ && rm -rf /var/lib/apt/lists/*

EXPOSE 8080
WORKDIR /app

COPY model_file.pkl constans.py app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
