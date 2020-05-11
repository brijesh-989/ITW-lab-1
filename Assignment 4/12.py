from array import *
user_in = array('i',[])
user=int(input("enter how many you want to add in your array : "))
for i in range(0,user):
    user_in.insert(0,int(input("enter numbers ny enter sepated : ")))
print(user_in.tolist())