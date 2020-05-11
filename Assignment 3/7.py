a=[1,2,3,4,5,6,(1,2)]
counter=0
for i in a:
    if type(i) == tuple:
        break
    else:
        counter=counter+1
print(counter)