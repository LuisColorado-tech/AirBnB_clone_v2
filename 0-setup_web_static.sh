#!/usr/bin/env bash
# script set web servers for the deployment of web_static

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create test html file
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give owner of the /data/ folder to ubuntu user and groups
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (https://mydomainname.tech/hbnb_static)
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# restart server
sudo service nginx restart