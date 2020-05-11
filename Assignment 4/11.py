user_in=input("enter a sequence of  numbers : ")
a=user_in.split(",")
for i in a:
    a=int(int(i,2))
    if a%5 == 0:
        print(i)