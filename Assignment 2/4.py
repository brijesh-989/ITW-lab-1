s=input("Enter the file name :")
f=open(s,'r')
contents = f.readlines()
n=int(input("Enter the last n lines : "))
while n > 0:
    print(contents[len(contents)-n])
    n=n-1
f.close()