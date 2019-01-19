n = int(input(""))
s = input("")
k = s.rfind('0',0,n)
c = 0
for i in range(k):
    if(s[i] != '0'):
        if(c ==0):
            c+=1
            print(s[i],end = "")
        else:
            print("",s[i],end = "")
