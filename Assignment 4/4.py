def insert_string(a,b):
    c=len(a)
    d=c//2
    print(a[:d]+b+a[d:])

user_string1=input("enter a outer string ")
user_string2=input("enter a middle string ")    
insert_string(user_string1,user_string2)