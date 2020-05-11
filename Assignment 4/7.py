def fact(a):
    if a==1:
        return 1
    elif a==0:
        return 1
    else:
        return a*fact(a-1)
      
def ncr(n,r):
        return fact(n)//(fact(r)*fact(n-r))
user_in=int(input("Enter number of rows you want to print : "))
a=user_in
for i in range(0,a):
    print(" "*(a+1))
    s=' '
    for j in range(0,i+1):
        s=s+" "+str(ncr(i,j))
    print(s)
    a=a-1   