user_input1=list(map(str,input("enter a first list : ").split()))
user_input2=list(map(str,input("enter the second list : ").split()))
for (a,b) in zip(user_input1,user_input2):
    print(a, b) 