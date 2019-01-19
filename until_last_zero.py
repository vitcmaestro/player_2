import collections
n = int(input(""))
s = input("")
k = s.rfind('0',0,n)
c = 0
freq = collections.Counter(s)
if(freq['0'] == 1):
    for i in range(0,k):
        print(s[i],end="")
else:
    for i in range(k):
        if(s[i] != '0'):
            if(c ==0):
                c+=1
                print(s[i],end = "")
            else:
                print("",s[i],end = "")
