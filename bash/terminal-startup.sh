#### Al of this is in the .bash_profile file


# Enable tab completion for git
source ~/git-completion.bash

# Colors
green="\[\033[0;32m\]"
blue="\[\033[0;34m\]"
purple="\[\033[0;35m\]"
reset="\[\033[0m\]"

# Change command prompt
source ~/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1="$purple\u$green\$(__git_ps1)$blue \W $ $reset"

# Start shellmarks
source ~/.local/bin/shellmarks.sh