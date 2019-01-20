import collections
n,k = map(int,input().split())
mem = list(map(int,input().split()))
dic = collections.Counter(mem)
print(dic[k])
