def rep(b):
    for d in b:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V + VI'] = (n1+n2)/2
    
    print(b)
    
a=int(input("how many dictionary you wan to enter: "))
b=[]

for i in range(a):
    d={}
    d['id'] = input("enter the id ")
    d['subject'] = input("enter the subject ")
    d['V'] = int(input("enter the value of V "))
    d['VI'] = int(input("enter the value of VI "))
    b.append(d)    
rep(b)    
    