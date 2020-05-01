import os

os.chdir("A:\T_H\python_study\ch05")
os.system("dir")
f=os.popen("dir")
print(f)