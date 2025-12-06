# Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy everything from current folder to /app in container
COPY . .

#install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start the Flask app
CMD ["python3", "app.py"]
