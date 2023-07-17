# Dockerfile
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Expose port for Nginx
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
