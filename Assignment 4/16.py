from array import *
array_num = array('i',[])
a=int(input("Enter how many elements :"))
for i in range(a):
    array_num.append(int(input()))
c=array_num.tolist()
print(c)