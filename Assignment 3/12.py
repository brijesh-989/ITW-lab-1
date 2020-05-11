def rec_sum(l):
    ans=0
    for i in l:
        if type(i) ==type(list()):
            ans = ans + rec_sum(i)
        else:
            ans = i + ans
    return ans
l=[1,2,[3,4],[5,6]] 
print(rec_sum(l))           