import geocoder

g = geocoder.ip('123.456.789.012') # 외부 ip 직접 설정
#g = geocoder.ip('me') // 자신의 ip로 위치 설정
print(g.latlng)
print(g.city)