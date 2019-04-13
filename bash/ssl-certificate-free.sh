###
### Using Google Cloud and Bitnami Wordpress stack
###

## From youtube video: https://www.youtube.com/watch?v=DBnQkH1v-Xw

## Install git
sudo su
sudo apt-get install git-all
# the above didn't work for me (11/27/17) so I did the following:
sudo apt-get install git
# then that didn't work for me (12/5/17) so I did the following:
sudo apt-get update
sudo apt-get install git

## Go to tmp directory and install certbot
cd ../..
cd /tmp
git clone https://github.com/certbot/certbot

## Go to certbot directory and install certificates
cd certbot
./certbot-auto certonly --webroot -w /opt/bitnami/apps/wordpress/htdocs/ -d metapp.org -d www.metapp.org
./certbot-auto certonly --webroot -w /opt/bitnami/apps/wordpress/htdocs/ -d http://35.196.166.27
cd
## Test auto-renewal
./certbot-auto renew --dry-run

## Setup auto-renewal
crontab -e
1

    ## Add these lines
    #0 0 * * * cd && ./certbot-auto renew --quiet --no-self-upgrade 
    #0 12 * * * cd && ./certbot-auto renew --quiet --no-self-upgrade
    # Once a week on Friday
    0 0 * * 6 cd /tmp/certbot && ./certbot-auto renew && /opt/bitnami/ctlscript.sh restart apache

    # Every night at midnight
    0 0 * * * cd /tmp/certbot && ./certbot-auto renew && /opt/bitnami/ctlscript.sh restart apache

## Save
ctrl + o
ENTER
## Exit
ctrl + x

## Add an automatic redirect to https
sudo su
nano /opt/bitnami/apache2/conf/bitnami/bitnami.conf

    ## Comment the old certificate files and paste these underneath
    SSLCertificateFile "/etc/letsencrypt/live/duncanrager.com/cert.pem" 
    SSLCertificateKeyFile "/etc/letsencrypt/live/duncanrager.com/privkey.pem" 
    SSLCertificateChainFile "/etc/letsencrypt/live/duncanrager.com/fullchain.pem"

    ## And add these underneath DocumentRoot at the top to automatically redirect things to https
    RewriteEngine On
    RewriteCond %{HTTPS} !=on
    RewriteRule ^/(.*) https://%{SERVER_NAME}/$1 [R,L]

## Restart server
sudo /opt/bitnami/ctlscript.sh restart apache

## Test certificate here
https://www.ssllabs.com/ssltest/
