def list_slice(d,e):
    return [d[i::e] for i in range(e)]
a=list(map(str,input("enter the character sepated by space : ").split()))
b=int(input("enter the Nth value of slicning : "))
print(list_slice(a,b))