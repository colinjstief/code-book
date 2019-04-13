## Check for existing SSH keys
ls -al ~/.ssh

## Create new SSH key pair
ssh-keygen -t rsa -b 4096 -C 'colin.stief@gmail.com'

## Start SSH agent
eval "$(ssh-agent -s)"

## Tell agent where key lives
ssh-add ~/.ssh/id_rsa

## Copy contents of key to clipboard
pbcopy < ~/.ssh/id_rsa.pub

## Use SSH to test connection
ssh -T git@github.com

## Push up to Github
git remote add origin https://github.com/colinjstief/web_server.git
git push -u origin master