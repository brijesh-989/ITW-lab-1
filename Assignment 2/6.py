s=input("Enter the file name :")
f=open(s,'r')
print(len(f.readlines()))
f.close()