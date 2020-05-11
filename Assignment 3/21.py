import random
a,b,c = input("Enter the dates 1 : ").split("/")
d,e,f = input("Enter the dates 2 : ").split("/")
g=random.randint(int(a),int(d))
h=random.randint(int(b),int(e))
i=random.randint(int(c),int(f))
print(f" Random dates is : {g}/{h}/{i}")
