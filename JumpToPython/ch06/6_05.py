import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab = f.read()
f.close()

space = tab.replace("\t", "" * 4)

f = open(dst, 'w')
f.write(space)
f.close()

#python 6_05.py src dst