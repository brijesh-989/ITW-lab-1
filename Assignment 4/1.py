user_string = input("enter a string :")
if len(user_string) > 1:
    print(user_string[0:2]+user_string[-2]+user_string[-1])
else:
    print("Empty String")