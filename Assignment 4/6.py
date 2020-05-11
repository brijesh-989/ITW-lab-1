user_string = input("Enter a string : ")
s=set(user_string)

for i in s:
    counter=0
    for j in user_string:
        if i == j:
            counter+=1
    print(f"{i} {counter}")