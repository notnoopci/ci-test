FROM dockerfile/nginx

ADD default /etc/nginx/sites-enabled/default
ADD public /var/lib/nginx/public