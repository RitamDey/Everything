# ZSH Theme - Preview: http://gyazo.com/8becc8a7ed5ab54a0262a470555c3eed.png

local user='%{$terminfo[bold]$fg[cyan]%}%n%{$reset_color%}'
local host='%{$terminfo[bold]$fg[green]%}%m%{$reset_color%}'
local current_dir='%{$terminfo[bold]$fg[blue]%}%c%{$reset_color%}'
local at='%{$terminfo[bold]$fg[red]%}at%{$reset_color%}'
local in='%{$terminfo[bold]%}in%{$reset_color%}'

local git_branch='$(git_prompt_info)%{$reset_color%}'

PROMPT="${user} ${at} ${host} ${in} ${current_dir}
%B➜%b "
RPS1="%B${git_branch}%b"

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[yellow]%}‹"
ZSH_THEME_GIT_PROMPT_SUFFIX="› %{$reset_color%}"

