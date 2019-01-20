n = int(input(""))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c =[]
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j] and a[i] not in c):
            c.append(a[i])
d = 0        
for i in c:
    if(d==0):
        d+=1
        print(i,end = "")
    else:
        print("",i,end ="")
