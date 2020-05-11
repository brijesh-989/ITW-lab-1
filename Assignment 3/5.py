#L=[(),(),("",),('a','b','c'),('a','b'),('d')]
a=int(input("How mant you want to enter :"))
b=[]
for i in range(a):
    c=tuple(map(str,input("enter the values :").split()))
    b.append(c)
print(b)    
b=[l for l in b if l]
print(b)