n = int(input())
mem = list(map(int,input().split()))
ans = []
for i in mem:
    if(i<n):
        ans.append(i)
ans.sort()
c =0
for i in ans:
    if(c==0):
        print(i,end ="")
        c+=1
    else:
        print("",i,end = "")
