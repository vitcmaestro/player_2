s1,s2 = map(str,input("").split())
if(len(s1)!=len(s2)):
    print("no")
else:
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            print("no")
            break
    else:
        print("yes")
