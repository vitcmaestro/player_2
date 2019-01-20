import collections
n = int(input())
mem = list(map(str,input().split()))
dic = dict(collections.Counter(mem))
maxer = 0
for x,y in dic.items():
    if(y>maxer):
        ans = x
        maxer = y
print(ans)
