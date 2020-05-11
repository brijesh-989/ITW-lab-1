def merge(l1,l2):
    d={}
    j = 0
    for i,j in zip(l1,l2):
        d[i] = (j)
    print(d)
l1 = input("Enter the first list").split()
l2=input("Enter the second list").split()
print(merge(l1,l2))             