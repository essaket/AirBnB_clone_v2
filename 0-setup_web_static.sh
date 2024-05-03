#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update package lists to ensure we have the latest information
sudo apt-get update

# Install Nginx web server
sudo apt-get -y install nginx

# Allow HTTP traffic through the firewall for Nginx
sudo ufw allow 'Nginx HTTP'

# Create necessary directories for storing web_static content
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file inside the 'test' directory
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the 'test' directory in 'current' for easier referencing
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the '/data' directory to the user 'ubuntu'
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration file to include a location block for serving static files
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the changes
sudo service nginx restart
