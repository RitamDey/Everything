" Genral configs
set nocompatible
set number

" Enable filetype plugins
filetype plugin on
filetype indent on

" With a map leader it's possible to do extra key combinations
" like <leader>w saves the current file Plugin configs
let mapleader = ","
let g:mapleader = ","

" Fast saving
nmap <leader>w :w!<cr>
" Fast closing buffer
nmap <leader>q :q<cr>
" Fast saving and closing
nmap <leader>wq :wq<cr>

"" Backups while editing file
set backup
set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set backupskip=/tmp/*,/private/tmp/*
set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
set writebackup


" VIM user interface
" Turn on wild menu
set wildmenu

" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
    set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_STORE
else
    set wildignore+=.git\*,.hg\*,.svn\*
endif

" Always show current position
set ruler

" Height of command bar
set cmdheight=2

" Configure backspace so it act as it should
set backspace=eol,start,indent
set whichwrap=<,>,h,l

" In many terminals mouse works, enable it
if has('mouse')
    set mouse=a
endif

" Ignore case when searching
set ignorecase

" When searching try to be smart about cases
set smartcase

" Hightlight search results
set hlsearch

" Makes search act like search in mordern browsers
set incsearch


"" Colors and Fonts
" Enable syntax hightling
syntax enable

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8

" Use Unix as the standard file type
set ffs=unix,dos,mac


"" Text, Tab and indent related settings
" Use spaces instead of tabs
set expandtab

" Be smart when using tabs
set smarttab

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4

" Line break on 500 charachters
set lbr
set tw=500

set ai " Auto-indent
set si " Smart Indent
set wrap " Wrap lines

" Remember the last position in the file
if has("autocmd")
    au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\""
endif

"" Tabs, and windows settings
" Useful tab mappings
map <leader>t :tabnew<cr>
map <leader>tc :tabclose<cr>
map <leader>tn :tabnext<cr>
map <leader>tp :tabprevious<cr>

" Let 'tl' toggle between this and the last accessed tab
let g:lasttab = 1
nmap <leader>tl :exe "tabn ".g:lasttab<CR>
au TabLeave * let g:lasttab = tabpagenr()


set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#begin('~/.config/nvim/bundle')

Plugin 'VundleVim/Vundle.vim'

call vundle#end()
filetype plugin indent on


""" General stuff
set laststatus=2


""" Python stuff
set showmatch
let python_highlight_all = 1


