#  w* use to check alphanumeric value

import re
text="I Love Lion 1234567. they are 1234 Lion"
pattern=r'\W*'

res=re.split(pattern,text)
print(res)
