s=input("Enter the file name :")
f=open(s,'r')
a=f.read()
contents = list(map(list,a.split())) 
for i in range(len(contents)):
    contents[i] = (''.join(contents[i]))
print(contents)    
d={}
for i in contents:
    d[i] = contents.count(i)
print(d)  
f.close()