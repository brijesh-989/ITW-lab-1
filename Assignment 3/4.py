
a=int(input("how many items you want to enter in a list :"))
b=[]
for i in range(a):
    d = tuple(map(str,input("enter the item no and value separated by ',' :").split(',')))
    b.append(d)   
print(sorted(b, key= lambda x : int(x[1]),reverse=True))
   
    