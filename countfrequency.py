ls=[1,2,3,4,6,8,4,2,1,4]
d={}
for i in ls:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)
