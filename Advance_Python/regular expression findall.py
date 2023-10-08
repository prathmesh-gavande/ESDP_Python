import re
text="I Love Lion . they are Lion"
pattern=r"Lion"

res=re.findall(pattern,text)
print(res)

