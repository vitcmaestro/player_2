import collections
s,k = map(str,input("").split())
dic = dict(collections.Counter(s))
print(dic[k])
