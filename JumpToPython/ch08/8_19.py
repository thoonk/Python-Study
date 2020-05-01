#번호 뒷자리 4개를 ####로 바꾸시오
data ="""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

import re

p = re.compile("\d{3}[-]\d{4}[-](\d{4})")
result = p.sub("\g<1>-####", data)

print(result)
