import re
p = re.compile("[a-z]+")
m = p.search("5 python")

print(m.start() + m.end())
#결과 값  8 + 2 = 10