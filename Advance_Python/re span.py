#  w* use to check alphanumeric value

import re
text="I Love Lion 1234567. they are 1234 Lion"
pattern=r'[A-Z]+ion'

res=re.finditer(pattern,text)
for i in res:
    print(i.span())
