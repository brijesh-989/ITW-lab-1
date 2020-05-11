from array import *
array_num = array('i',[])
a=int(input("Enter how many elements in an array : "))
for i in range(a):
    array_num.append(int(input("enter the numners in an array by enter sepated : ")))
a=int(input("enter the numbers you have to find its accurance : "))

print(f"occurance of{a} -->{array_num.count(a)}")