# You're not wrong, your bitnami probably has it's own webserver which it starts and also uses it on port 80. 
# Now you installed a package that installed apache2 aswell, which now blocks port 80 since it's using it.

# Now your bitnami webserver cannot bind to the - in use - port 80 and fails to start.

# Since your configuration is only available at the bitnami one you only get the default page which is provided in /var/www

# Long story short, disable and stop the newly installed apache2 service.

sudo systemctl stop apache2.service && sudo systemctl disable apache2.service
sudo /opt/bitnami/ctlscript.sh restart apache

# After that run your start script again and it should work.

# Question will arise again though how you want the plugin to work if you are using the system to install it but 
# use an externally installed apache2 service. You'll probably need to install the plugin via bitnami aswell.