from array import *
array_num=array('i',[])
array_num1=array('i',[])
m=int(input('how many numbers you wantto enter in both array'))
for i in range(m):
    array_num.append(int(input("enter numbers for array 1 entered separated : ")))
for i in range(m):
    array_num1.append(int(input("enter numbers for array 2 enter sepated : ")))  
li = array_num1+array_num
print(sorted(li.tolist()))      
    
    