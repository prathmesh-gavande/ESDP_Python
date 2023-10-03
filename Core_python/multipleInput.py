l=list(map(int,input().split()))

key=int(input("Enter any number: "))

for i in range (len(l)):
    if key==l[i]:
        print("Key is found at a index : ",i+1)
        break
else:
    print("Key is not found.")