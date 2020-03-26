# Columnar
A more complex scheme is to write the message in a rectangle, row by row, and read the message off, column by column, but permute the order
of the columns. The order of the columns then becomes key to the algorithm. For example,
Input: Welcome to india dear
Key           :       c  o  n  v  e  r  t
Input         :       w  e  l  c  o  m  e
                      t  o  i  n  d  i  a
                      d  e  a  r  
        
Output        :      wtdodxliaeoemixeaxcnr
