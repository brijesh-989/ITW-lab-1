big=[]
s1=int(input("enter how many sublist you want to enter in a list : "))
for i in range(1,s1+1):
    a=list(map(int,input(f"enter the numbers in a {i} sub list then press enter : ").split()))
    big.append(a)  
Sample=big
for i in Sample:
    if Sample.count(i) > 1:
        Sample.remove(i)
print(Sample)