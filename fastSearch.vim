if !has('python')
  finish
endif
function! FastSearch(query)
pyfile fastSearch.py
endfunction

command! -nargs=1 Fs call FastSearch(<f-args>)
