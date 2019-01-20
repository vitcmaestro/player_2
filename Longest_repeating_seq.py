import collections
n = int(input())
mem = list(map(str,input().split()))
maxer = 1
start = mem[0]
c = 1
for i in range(1,len(mem)):
    if(start == mem[i]):
        c = c+1
        if(c>maxer):
            maxer = c
    else:
        start = mem[i]
        c = 1
print(maxer)
    
