import vim

def fastSearch(query):

  row = 1                                   # vim cursor 1-base idx
  for line in vim.current.buffer:
    col = line.find(query)

    if col != -1:                           # stop and move cursor
      vim.current.window.cursor = (row, col)
      return
    else:                                   # not in line, cont. search
      row = row + 1

  print "Query not present."


def main():
  fastSearch(vim.eval("a:query"))   # extract query argument from vim script

main()
