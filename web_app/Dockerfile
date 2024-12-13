# syntax=docker/dockerfile:1

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY web_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY web_app/ .

# Install Node.js for Next.js
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g n && \
    n stable && \
    apt-get purge -y nodejs npm

# Install dependencies for Next.js
WORKDIR /usr/src/app/frontend
COPY web_app/frontend/package.json web_app/frontend/package-lock.json ./
RUN npm install

# Build the Next.js app
RUN npm run build

# Add entrypoint script
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Expose the port the app runs on
EXPOSE 8000

# Start the application
CMD ["gunicorn", "--chdir", "web_app", "--bind", ":8000", "web_app.wsgi:application"]