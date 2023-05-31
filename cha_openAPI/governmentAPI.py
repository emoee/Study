import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree  as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd
import time
import folium
import ast


cnt = 1
heritages = []
#heritages.append(["문화재종목", "문화재명(국문)", "문화재명(한자)", "시도명", "시군구명", "관리자", "경도", "위도"]) #데이터 값
for page in range(1, 2): #데이터가 총 16784개이다.
    url = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do?pageUnit=999&pageIndex=%d"%page #999개씩 17번 검색
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    doc =  ET.fromstring(str(soup))
    items = doc.iter(tag="item")
    for item in items:
        ccmaname = item.find('ccmaname').text  #문화재종목
        name = item.find('ccbamnm1').text #문화재명(국문)
        name2 = item.find('ccbamnm2').text #문화재명(한자)
        city = item.find('ccbactcdnm').text #시도명
        city2 = item.find('ccsiname').text #시군구명
        admin = item.find('ccbaadmin').text #관리자
        longitude = item.find('longitude').text #경도
        latitude = item.find('latitude').text #위도
        heritages.append([ccmaname, name, name2, city, city2, admin, longitude, latitude])

print(len(heritages))

MAP = folium.Map(location=[37.55, 127.55], zoom_start= 10, tiles='Stamen Terrain')
for map in heritages:
   folium.Marker([float(map[7]), float(map[6])], icon=folium.Icon(color="green"), popup='<b>%s</b>'%map[1], tooltip='<i>%s</i>'%map[0]).add_to(MAP)

MAP.save("./map.html")