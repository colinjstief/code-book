###
### Using Google Cloud and Bitnami Wordpress stack
###

## 1. Download PuttyGen
## 2. Generate a key
## 3. Replace comment with username, and optionally add a password
## 4. Save private key
## 5. Save public key
## 6. Export > OpenSSH for the open source version of the key
## 7. Go to metadata page of project and add the text from PuttyGen
## 8. Use external IP and public/private key for SFTP settings

## 9. Change owner of htdocs directory (and subfolders/files) to bitnami and group to daemon
sudo chown -R bitnami:daemon /opt/bitnami/apps/wordpress/htdocs

## 10. Give write permission to the same folder
sudo chmod -R g+w /opt/bitnami/apps/wordpress/htdocs

## For more info -- http://linuxcommand.org/