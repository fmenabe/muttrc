"" General parameters.
set nocompatible
set nu
set autoindent
set backspace=indent,eol,start
set listchars=trail:◃,nbsp:•


"" Persistent undo.
set undofile
set undodir=$HOME/.vim/undo
set undolevels=1000
set undoreload=10000


"" Tabs and spaces parameters.
set expandtab
set tabstop=2
set softtabstop=2
set shiftwidth=2


"" Search parameters.
set hlsearch
set incsearch


"" Colors and cursor.
set t_Co=256
set background=light
colorscheme solarized
set scrolloff=999 " cursor always in the middle of the screen
set cursorline
highlight CursorLine cterm=none
set cursorcolumn
highlight CursorColumn cterm=none


"" Keys mapping
map <F1> :set nu!<CR>
map <F2> :set paste! <bar> :set paste?<CR>
map <F3> :set list!<CR>
map <F4> :set ignorecase! <bar> :set ignorecase?<CR>
map <F5> :let @/=""<CR>
map <F6> m<Space><CR>
map <F7> :set hlsearch!<CR> :set hlsearch?<CR>
