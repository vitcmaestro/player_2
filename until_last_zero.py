n = int(input(""))
s = input("")
k = s.rfind('0',0,n)
for i in range(k):
    if(s[i] != '0'):
        print(s[i],end = "")
