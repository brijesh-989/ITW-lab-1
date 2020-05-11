a=list(map(int,input("enter the numbers : ").split()))
string = input("enter the string : ")
for i in range(0,len(a)):
    a[i] = string+str(a[i])
print(a)