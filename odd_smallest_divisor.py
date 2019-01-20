n = int(input(""))
for i in range(1,n):
    temp = n%i
    if(temp == 0 and (n/i)%2 != 0):
        print(i)
        break
