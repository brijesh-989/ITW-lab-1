s=input("Enter the file name 1 :")
f=open(s,'r+')
q=input("Enter the file name 2 :")
f1=open(q,'r+')
a=list(f.read())
b=[]
z=""
c=list(f1.read())
d=[]
r=""
for i in a:
    if i == ',' or  i =='(' or i==')':
        b.append(z)
        z=""
    else:
        z=z+i
for i in c:
    if i == ',' or  i =='(' or i==')':
        d.append(r)
        r=""
    else:
        r=r+i           
e=input("Enter the name of file 3 : ")
f2=open(e,'a+')
for i,j in zip(b,d):
    f2.write(f"{i}\n{j}\n")