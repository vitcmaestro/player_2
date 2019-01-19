import collections
s = input("").split()
subs = input("")
count = 0
for words in s:
    if words  == subs:
        count+=1
print(count)
