## Print current directory
pwd

## Change directory
cd Desktop
cd Desktop/github/projects/my-project
cd ..  # up a directory
cd ~   # home

## List contents of current directory
ls
ls -l # view contents as list with permissions
ls -a # view hidden files

## Create new directory
mkdir new-folder
mkdir -p parent-directory/sub-directory                     # use the -p flag to create parent and sub-directory with one line
mkdir -p parent-directory/{sub-directory-a,sub-directory-b} # same as above, but use curly brackets to create multiple sub-directories in same parent

## Create new file
touch new-file.txt
touch new-file.html diff-file.js

## Copy file
cp file.sh new-filename.js
cp file.sh directory/new-filename.js    # different directory
cp -r directory new-directory           # all files into another directory

## Move file
mv file.sh directory
mv file.sh dif-file.sh directory         # multiple files
mv file.sh directory/new-filename.js     # and rename the file

## Delete file
rm file.sh
rm file.sh dif-file.sh                   # multiple files
rm -r directory                          # entire directory