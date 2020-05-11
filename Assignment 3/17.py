def my(a):
    b=[]
    for i in a:
        b.insert(0,i)

    return ' '.join(b)
a= map(str,input("Enter the string ").split())
print(my(a))