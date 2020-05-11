from array import *
array_num = array('i',[])
a=int(input("Enter how many elements :"))
for i in range(a):
    array_num.append(int(input("enter the numbers in an array by enter separated : ")))
b=int(input("enter the position you want to delete : "))
del array_num[b+1]
print(array_num.tolist())