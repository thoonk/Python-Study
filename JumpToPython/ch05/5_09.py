import sys

num = sys.argv[1:]
result=0;
for n in num:
    result+=int(n)
print(result)