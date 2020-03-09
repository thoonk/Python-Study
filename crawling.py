import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.acmicpc.net/contest/official/list')
soup=BeautifulSoup(res.content, 'html.parser')


#타이틀 가져오기
print(soup.head.title)

#모든 메타 데이터의 내용 가져오기
for meta in soup.head.find_all('meta'):
    print(meta.get('content'))

#테이블 태그 관련 정보 가져오기
for link in soup.find_all('table'):
    print(soup.get_text())
all_tb=soup.find_all("table")
print(all_tb)

#모든 링크의 텍스트와 주소 가져오기
for link in soup.find_all('a'):
    print(link.text.strip(), link.get('href'))