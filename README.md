# fastSearch-vimplugin

When searching over large files, vims usual regex search "/ query" is
slow.

This vim plugin defines :Fs, called as ":Fs query".

:Fs is an efficient search command over the vim buffer using
a Boyer-Moore-Horspool search algorithm - python's str.find().

As a result :Fs is much quicker for searching raw strings, then
vims regex search.

Note: Query will be searched as a raw string. :Fs does not parse any special
characters; it cannot perform a regex search. 

