import vim

def fastSearch(query):

  (row, col) = vim.current.window.cursor    # get current position.
  current_line = vim.current.buffer[row-1]
  current_line = current_line[col:]         # take unsearched portion
  search_pos = current_line.find(query)     # search current line.


  if search_pos == 0:                     # match under cursor
    current_line = current_line[1:]         # move forward in line 
    search_pos = current_line.find(query)   # re-search line
    if search_pos != -1:
      vim.current.window.cursor = (row, col + search_pos+1) # calib for slice
      return

  if search_pos == -1:                      # no match in current line.
    row = row + 1
    if row == len(vim.current.buffer) + 1:  # reached end
      row = 2                               # so loop
      print "Continue from top"
  else:                                     # genuine next match in line
    vim.current.window.cursor = (row, col + search_pos)  # calib for slice
    return


  for line in vim.current.buffer[row-1:]:
    col = line.find(query)

    if col != -1:                           # stop and move cursor
      vim.current.window.cursor = (row, col)
      return
    else:                                   # not in line, cont. search
      row = row + 1

  print "FAIL: query not present."


def main():
  fastSearch(vim.eval("a:query"))   # extract query argument from vim script

main()

