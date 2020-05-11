s=input("Enter the file name : ")
f=open(s,'r')
a=[]
contents = f.readlines()
for i in contents:
    a.append(list(i.split()))   
print(a)