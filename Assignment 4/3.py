user_string=input("enter a string : ")
a=user_string.index('not')
b=user_string.index('poor')
if a < b :
    print(user_string[0:a]+"good "+ user_string[b+5:]) 
else: 
    print(user_string)