user_in=input("enter a string : ")
count=0
cint=0
for i in user_in:
    if i.isupper() == True:
        count+=1
    elif i.islower() == True:
        cint+=1
print(f"No of upper case characters are : {count}") 
print(f"No of upper lower characters are : {cint}")  