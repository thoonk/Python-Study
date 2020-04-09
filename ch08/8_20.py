#다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다.
# 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.

#.*[@].*[.].*$

'''
park@naver.com
kim@daum.net
lee@myhome.co.kr
'''

import re

p = re.compile(".*[@].*[.](?=com$|net$).*$")

print(p.match("park@naver.com"))
print(p.match("kim@daum.net"))
print(p.match("lee@myhome.co.kr"))
