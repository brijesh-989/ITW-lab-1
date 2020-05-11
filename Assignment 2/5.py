s=input("Enter the file name : ")
txt=open(s,'r')
list_=[(),()]
tuple_=tuple(map(str,txt.read().split()))                
list_.append(tuple_)                                     
ans=[]
for i in list_:
    if i!=():
      ans.append(i)

print(ans)