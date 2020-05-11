def tup(l):
    e={}
    for i,j in l:
        d={}
        d[j] = int (i)
        e.update(d)
    return e
l=((2,"W"),(3,"R"))
a=int(input("Enter how many tuples you want to enter : "))
b=[]
for i in range(a):
    c=tuple(input("enter the value and key sepaerted by ','").split(","))
    b.append(c)   
l=tuple(b)   
print(tup(l))    