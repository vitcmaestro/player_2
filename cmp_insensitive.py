s3,s4 = map(str,input("").split())
s1 = s3.lower()
s2 = s4.lower()
if(len(s1)!=len(s2)):
    print("no")
else:
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            print("no")
            break
    else:
        print("yes")
