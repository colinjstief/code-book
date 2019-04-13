## Loop through files in pwd
for file in *; do echo $file; done

## Loop through files with particular ending in pwd
for file in *.jpg; do echo $file; done

## Loop through file with particular ending in pwd, 
## remove the last 11 characters, and add a new extension
for file in *58-150x150.jpg;
do
    newname=${file::-11};
    newextension='300x300.jpg';
    echo $newname$newextension; 
done

## Loop through file with particular ending in pwd, 
## remove the last 11 characters, add a new extension
## and copy it using the new name
for file in *58-150x150.jpg;
do
    newname=${file::-11};
    newextension='300x300.jpg';
    cp $PWD/$file $PWD/$newname$newextension; 
done

## Loop through all files recursively (in sub-folders)
## On Mac with new string replacement syntax

for file in $(find ./uploads -name "*.jpg");
do
    newextension='300x300.jpg';
    ## String replacement on Mac OSx
    echo ${file/150x150.jpg/$newextension}; 
done

for file in $(find ./uploads -name "*150x150.jpg");
do
    newextension='300x300.jpg';
    filename=${file/150x150.jpg/$newextension};
    finalname=${filename/.\/uploads/uploads};
    cp $PWD/$file $PWD/$finalname;
done