###
### Initializing
###

git init                                                                # In project's root folder
# Create .gitignore                                                     # Ignore files/folders, usually node_modules/
git add .
git commit -m 'initial commit'                                          # Commit first changes
# Create new repository @GitHub
git remote add origin https://github.com/colinjstief/repo-name.git      # This is code copied from GitHub
git push -u origin master

###
### Typical flow
###
git checkout -b new-feature             # Create new branch for developing a feature
        ## develop!
git status                              # Look at what has changed
git add -A                              # Stage all changes
git commit -m "Completed new feature"   # Commit changes
git checkout master                     
git merge new-feature --no-ff           # Merge development branch to master branch with dedicated commit for merge differences
git push origin master                  # Push changes to GitHub remote repository
        ## pull request in GitHub


###
### Creating repositories and remotes
###

## Create new repository in current directory
git init

## View remotes
git remote
git remote add origin https://url.github.com/repo   # add new remote and name it origin if it is the first

## Clone repository
git clone https://my.github.repository/cool-repository

###
### Viewing history
###

## List commits
git log
git log other-branch    # other than current
git log -10             # limit to certain number
git log --oneline       # less detail
git log --graph         # branch visualization

## Find differences in files
get diff                        # between working directory and staging area
get diff --staged               # between staging area and repository
git diff file.js dif-file.js    # specific files in repository

## Check differences detected
git status

###
### Committing changes
###

## Put the changes up on the staging area
git add
git add -A   # stages all; combines the two commands below
git add .    # stages new and modified, without deleted
git add -u   # stages modified and deleted, without new

# Rollback changes
git reset           # remove staged changes from staging error
git reset --hard    # remove changes completely from the file

## Make a commit to the repository
git commit      # automatically opens editor for a message if your config is set
git commit -m "Make this change"  # add a message manually
ESC --> :wq     # exit the add message

## Send commits to a remote repository... usually on GitHub
git push
git push branch     # push a specific branch

git pull


###
### Branches
###

## List branches
git branch              # the asterisk (*) shows which is currently checked out

## Create new branch
git branch new-branch
git branch -b new-branch  # create new branch and retain current commits
git branch -d new-branch  # delete branch label, but keep the commit history

## Checkout old version
git checkout [commit-id or branch]
git checkout 25ede836903881848fea811df5b687b59d962da3
git checkout master
git checkout -          # go back to original after checkout

## Merge branches
git merge branch-name               # Merge to current branch
git merge branch-name --no-ff       # No fast forward option  --  :wq + enter to escape message
                                    # Create dedicated commit for a merge; good for looking at all the changes/commits in a particular branch

###
### Miscellaneous
###

## Check version
git --version