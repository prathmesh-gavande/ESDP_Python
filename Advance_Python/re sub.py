#  w* use to check alphanumeric value

import re
text="I Love Lion 1234567. they are 1234 Lion"
pattern=r' '

res=re.sub(pattern,"@",text)
print(res)
