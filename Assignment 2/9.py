s=input("Enter the file name :")
f=open(s,'a+')
l= input("enter the list sepated with space : ").split()
for i in l:
    f.write(i+"\n")
f=open(s,'r')
print(f.read())
f.close()