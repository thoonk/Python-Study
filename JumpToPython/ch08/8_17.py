#다음 중 정규식 a[.]{3,}b와 매치하는 문자열 ?

import re

p = re.compile("a[.]{3,}b")

print(p.match("a....b"))