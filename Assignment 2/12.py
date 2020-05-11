n=int(input("Enter how many lines you want to enter : "))
a=[]
for i in range(1,n+1):
    s=input(f"enter the sentence {i} separted by hit enter : ")
    a.append(s)
for i in a:
    print(i.upper())