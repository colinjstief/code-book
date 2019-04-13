
## Changing permissions to owner read/write/execute and everybody else read/execute
## 755 (rwxr-xr-x)

sudo chmod -R 755 /opt/bitnami/apps/wordpress/htdocs/wp-content/themes/met_theme/assets/images/numbered_markers

## Ownership of files
sudo chown -R bitnami:daemon /opt/bitnami/apps/wordpress/htdocs
sudo chmod -R g+w /opt/bitnami/apps/wordpress/htdocs