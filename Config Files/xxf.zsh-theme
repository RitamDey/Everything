# Copy and self modified from ys.zsh-theme, the one of default themes in master repository
# Clean, simple, compatible and meaningful.
# Tested on Linux, Unix and Windows under ANSI colors.
# It is recommended to use with a dark background and the font Inconsolata.
# Colors: black, red, green, yellow, *blue, magenta, cyan, and white.
#
# http://xiaofan.at
# 2 Jul 2015 - Xiaofan

# Machine name.
function box_name {
    [ -f ~/.box-name ] && cat ~/.box-name || echo $HOST
}

function git_prompt_info() {
  local ref
  local hex
  if [[ "$(command git config --get oh-my-zsh.hide-status 2>/dev/null)" != "1" ]]; then
    ref=$(command git symbolic-ref HEAD 2> /dev/null) || \
    ref=$(command git rev-parse --short HEAD 2> /dev/null) || return 0
    hex=$(command git rev-parse --short HEAD 2> /dev/null)
    echo "$ZSH_THEME_GIT_PROMPT_PREFIX${ref#refs/heads/}:${hex}$(parse_git_dirty)$ZSH_THEME_GIT_PROMPT_SUFFIX"
  fi
}

# Directory info.
local current_dir='${PWD/#$HOME/~}'


# VCS
YS_VCS_PROMPT_PREFIX1="%{$fg[white]%}on%{$reset_color%} "
YS_VCS_PROMPT_PREFIX2="%{$terminfo[bold]$fg[cyan]%}"
YS_VCS_PROMPT_SUFFIX="%{$reset_color%} "
YS_VCS_PROMPT_DIRTY=" %{$reset_color%}%{$fg[red]%}✗%{$reset_color%}"
YS_VCS_PROMPT_CLEAN=" %{$reset_color%}%{$fg[green]%}✔︎%{$reset_color%}"

# Git info.
local git_info=""
ZSH_THEME_GIT_PROMPT_PREFIX="${YS_VCS_PROMPT_PREFIX1}${YS_VCS_PROMPT_PREFIX2}"
ZSH_THEME_GIT_PROMPT_SUFFIX="${YS_VCS_PROMPT_SUFFIX}"
ZSH_THEME_GIT_PROMPT_DIRTY="$YS_VCS_PROMPT_DIRTY"
ZSH_THEME_GIT_PROMPT_CLEAN="$YS_VCS_PROMPT_CLEAN"


# Prompt format: USER at MACHINE in [DIRECTORY] on git:BRANCH STATE \n $ 
PROMPT="%{$terminfo[bold]$fg[cyan]%}%n %{$reset_color%}\
%{$fg[white]%}at \
%{$terminfo[bold]$fg[green]%}$(box_name) %{$reset_color%}\
%{$fg[white]%}in \
%{$terminfo[bold]$fg[yellow]%}%c%{$reset_color%} \
$(git_prompt_info) \

%{$terminfo[bold]$fg[white]%}› %{$reset_color%}"
