user_input1=list(map(str,input("enter a first list : ").split()))
ini = int(input("enter the number : "))
exp_out=[]
for i in range(1,ini+1):
    for j in user_input1:
        exp_out.append(j+str(i))
print(exp_out) 