def match(x,y):
    for i in x.keys():
        if x.get(i) == y.get(i):
            print(f"{i} is present in both x and y ")
x={'key1' : 1,'key2':3,'key3':3}
y={'key1':1,'key2':3}
match(x,y)    