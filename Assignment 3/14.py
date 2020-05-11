a = list(map(int,input("Enter the numbers separsted by space : ").split()))
for j in range(0,len(a)):
    for i in range (0,len(a)-1) :
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)        