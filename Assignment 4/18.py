big=[]
s1=int(input("enter how many sublist you want to enter in a list : "))
for i in range(1,s1+1):
    a=list(map(int,input(f"enter the numbers in a {i} sub list then press enter : ").split()))
    big.append(a)

usr_list=big
a=sum(usr_list[0])
b=0
for i in range(1,len(usr_list)):
    if sum(usr_list[i]) > a:
        a=sum(usr_list[i])
        b=i
print(usr_list[b])