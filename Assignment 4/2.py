user_string=input("enter a string : ")
a=user_string[0]
print(user_string.replace(user_string[0],'$',2).replace('$',a,1))