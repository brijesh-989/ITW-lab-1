import random
e=input("Enter the name of file 3 : ")
f=open(e,'r')
b=f.readlines()
c=len(f.readlines())
a=random.randint(0,c)
print(b[a])