###
### Using Google Cloud and Bitnami Wordpress stack
###

## Get an SSL certificate and follow the instructions!

## Add an automatic redirect to https
## /home/bitnami/apps/wordpress/conf/httpd-prefix.conf

RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^/(.*) https://%{SERVER_NAME}/$1 [R,L]