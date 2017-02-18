colorscheme Monokai 

"Vim config copied from Kali
set number
set showmatch
set autowrite

" Read configs if files have autocmd command in file
if has("autocmd")
    filetype plugin indent on 
endif

" Jump to the last position
if has("autocmd")
    au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
