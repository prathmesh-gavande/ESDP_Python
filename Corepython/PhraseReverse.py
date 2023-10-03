print("Enter the phrase : ")
st=input()

st1=""
st2=""

for i in range (len(st)-1,-1,-1):
    if st[i]==" ":
        st2=st2+st1[::-1]+" "
        st1=""
    st1=st1+st[i]
st2=st2+st1[::-1]

print(st2)