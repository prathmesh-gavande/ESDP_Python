l=[10,45,67,97,66,3,9]
n=len(l)
a=[0]*n

for i in range (n):
    a[i]=l[n-i-1]

print(a)