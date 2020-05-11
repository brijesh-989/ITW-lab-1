user_input1=list(map(str,input("enter a first list : ").split()))
user_input2 = list(map(str,input("enter the second list : ").split()))
color1=[]
color2=[]
for i in user_input1:
    if i in user_input2:
        pass
    else:
        color1.append(i)
for j in user_input2:
    if j in user_input1:
        pass
    else:
        color2.append(j) 
print(f"color1 - color2 {color1}")
print(f"color2 - color1 {color2}")   