import re
text="I Love Lion 0ion lion. they are Lion"
pattern=r"[A-Z0-9a-z]+ion"

res=re.findall(pattern,text)
print(res)

