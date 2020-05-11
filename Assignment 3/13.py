a=list(map(int,input("Enter the numbers separted by space : ").split()))
b=int(input("Enter the number you want to search :"))
a.sort()
l=0
r=len(a)
while l <= r:
    mid=(l+r)//2
    if a[mid] == b:
        print(f"{b} is found at postion {mid}")
        break
    elif a[mid] > b:
        r = mid-1
    elif a[mid] < b:
        l = mid + 1
if(r<=l):
    print("element not found")                
    

                    
