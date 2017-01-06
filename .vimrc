:set nu
:set ai
:set cursorline
:set bg=dark
:set tabstop=3
:set shiftwidth=3
:set scrolloff=3
:set foldenable
:set foldmethod=indent
:set foldcolumn=1
:set foldlevel=5
filetype indent on
:inoremap ( ()<Esc>i
:inoremap { {}<Esc>i
:inoremap [ []<ESC>i
:inoremap " ""<ESC>i
:inoremap ' ''<ESC>i
:inoremap < <><ESC>i
if has("multi_byte")
  if &termencoding == ""
     let &termencoding = &encoding
  endif
  set encoding=utf-8
  setglobal fileencoding=utf-8
  "setglobal bomb
  set fileencodings=ucs-bom,utf-8,latin1
endif
					
