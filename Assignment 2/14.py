import os
cwd =os.getcwd()
print(cwd)
try:
    os.mkdir("newdir")
except FileExistsError:
    print("Directory already exists")
with open(cwd+"/"+"myfile.txt",'w') as f:
    f.write("")
os.remove(cwd+"/"+"myfile.txt")
os.rmdir("newdir")