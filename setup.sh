#!/bin/bash

# Update system
apt update && apt -y dist-upgrade && apt -y autoremove
apt install -y curl git nodejs npm tor curl gnupg2 ca-certificates lsb-release nginx

# Clone the repo
mkdir /var/www/html/
cd /var/www/html/
git clone https://github.com/glenn-sorrentino/hlr-website.git
cd hlr-website/

# Create Tor configuration file
sudo tee /etc/tor/torrc << EOL
RunAsDaemon 1
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:80
EOL

# Restart Tor service
sudo systemctl restart tor.service
sleep 10

# Get the Onion address
ONION_ADDRESS=$(sudo cat /var/lib/tor/hidden_service/hostname)

# Configure Nginx
cat > /etc/nginx/sites-available/hush-line.nginx << EOL
server {
    listen 80;
    server_name localhost;
    root /var/www/html/hlr-website/;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
    
        add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
        add_header X-Frame-Options DENY;
        add_header Onion-Location http://$ONION_ADDRESS\$request_uri;
        add_header X-Content-Type-Options nosniff;
        add_header Content-Security-Policy "default-src 'self'; frame-ancestors 'none'";
        add_header Permissions-Policy "geolocation=(), midi=(), notifications=(), push=(), sync-xhr=(), microphone=(), camera=(), magnetometer=(), gyroscope=(), speaker=(), vibrate=(), fullscreen=(), payment=(), interest-cohort=()";
        add_header Referrer-Policy "no-referrer";
        add_header X-XSS-Protection "1; mode=block";
}
EOL

# Enable the Tor hidden service
sudo ln -sf /etc/nginx/sites-available/hush-line.nginx /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx

# Configure Nginx
cat > /etc/nginx/nginx.conf << EOL
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
events {
        worker_connections 768;
        # multi_accept on;
}
http {
        ##
        # Basic Settings
        ##
        sendfile on;
        tcp_nopush on;
        types_hash_max_size 2048;
        # server_tokens off;
        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;
        include /etc/nginx/mime.types;
        default_type application/octet-stream;
        ##
        # SSL Settings
        ##
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;
        ##
        # Logging Settings
        ##
        # access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
        ##
        # Gzip Settings
        ##
        gzip on;
        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
        ##
        # Virtual Host Configs
        ##
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
        ##
        # Enable privacy preserving logging
        ##
        geoip_country /usr/share/GeoIP/GeoIP.dat;
        log_format privacy '0.0.0.0 - \$remote_user [\$time_local] "\$request" \$status \$body_bytes_sent "\$http_referer" "-" \$geoip_country_code';

        access_log /var/log/nginx/access.log privacy;
}

EOL

if [ -e "/etc/nginx/sites-enabled/default" ]; then
    rm /etc/nginx/sites-enabled/default
fi
ln -sf /etc/nginx/sites-available/hush-line.nginx /etc/nginx/sites-enabled/
nginx -t && systemctl restart nginx || error_exit

# Check if Node.js and npm are installed
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null; then
    echo "Node.js and npm are required but not installed. Please install them and try again."
    exit 1
fi

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    echo "Creating package.json"
    cat > package.json <<- EOM
{
  "name": "my_website",
  "version": "1.0.0",
  "description": "My Website using HTML, CSS, JavaScript, and Markdown",
  "scripts": {
    "start": "browser-sync start --server --files '**/*'"
  },
  "dependencies": {},
  "devDependencies": {
    "browser-sync": "^2.27.7"
  }
}
EOM
fi

echo "
✅ Installation complete!
                                               
http://$ONION_ADDRESS
"

# Install dependencies
echo "Installing dependencies"
npm install

# Build static HTML
echo "Building static HTML"
cd js/
node build.js
cd output/
mv * /var/www/html/hlr-website/
systemctl restart nginx 