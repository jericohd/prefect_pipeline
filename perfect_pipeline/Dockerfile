FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the Prefect server port (optional, for Prefect UI)
EXPOSE 4200

# Run Prefect
CMD ["python", "prefect_pipeline.py"]
