import sys
def memSize(s):
    return sys.getsizeof(s)
a=input("Enter the string :")
print(memSize(a))