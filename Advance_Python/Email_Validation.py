import re

pattern = r'^[A-Za-z0-9.+-_]+@+[a-z]+\.+[a-z]+$'
text="abcd123@gmail.com"
res = re.match(pattern, text)

if res:
    print("Valid")
else:
    print("Invalid")
