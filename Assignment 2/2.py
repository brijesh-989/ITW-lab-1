fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    n=int(input("how many you want to print : "))
    for i in range(n):
        print(f.readline(),end="")
f.close()