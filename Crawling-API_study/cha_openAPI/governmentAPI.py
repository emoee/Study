import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree  as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pandas as pd
import folium
import matplotlib.pyplot as plt
import csv
import requests
import csv
import matplotlib.pyplot as plt

def heritages_data(heritages):
    # heritages.append(["문화재종목", "문화재명(국문)", "문화재명(한자)", "시도명", "시군구명", "관리자", "경도", "위도"]) #데이터 값
    for page in range(1, 17): # 데이터가 총 16784개이다.
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
            longitude = item.find('longitude').text #경도 (위치 없을 시 0으로 표시됨.)
            latitude = item.find('latitude').text #위도
            heritages.append([ccmaname, name, name2, city, city2, admin, longitude, latitude])

    print(len(heritages))
    
    # 지도위에 저장한 데이터의 위치를 표시한다. 
    MAP = folium.Map(location=[37.55, 127.55], zoom_start= 10, tiles='Stamen Terrain')
    for map in heritages:
        folium.Marker([float(map[7]), float(map[6])], icon=folium.Icon(color="green"), tooltip='<i>%s</i>'%map[1]).add_to(MAP)

    MAP.save("./cha_openAPI/map.html")

def Heritage_Categories():
    with open("./cha_openAPI/governments_data.csv") as f:
        data = csv.reader(f)
        next(data)
        result = {}
        for row in data:
            category = row[4]
            result[category] = result.get(category, 0) + 1

    categories = list(result.keys())
    counts = list(result.values())
    
    plt.style.use('seaborn-pastel')
    plt.rc('font', family='AppleGothic') # Mac 사용시 맑은 고딕은 한글깨짐 오류가 발생함.
    plt.bar(categories, counts)
    plt.ylabel('Count')
    plt.title('Cultural Heritage Categories')
    plt.xticks(rotation=90)
    #plt.show()
    plt.savefig('./cha_openAPI/Cultural Heritage Categories.png') # 이미지파일 저장


def heritages_event():
    url = "http://www.cha.go.kr/cha/openapi/selectEventListOpenapi.do?searchYear=2023&searchMonth=05"

    # API 요청 보내기
    response = requests.get(url)
    response.encoding = 'UTF-8'
    
    # 응답 처리
    if response.status_code == 200:
        print(response.text)
    else:
        print("API 요청에 실패했습니다.")
        
    ###수정중###
 
def main():
    heritages = []
    heritages_data(heritages)
    csv_heritages = pd.DataFrame(heritages, columns=('문화재종목', '문화재명(국문)', '문화재명(한자)', '시도명', '시군구명', '관리자', '경도', '위도'))
    csv_heritages.to_csv('./cha_openAPI/governments_data.csv', encoding='utf-8', mode='w', index=True) # csv 파일 저장
    del heritages[:] # 데이터 저장 후 요소 삭제
    Heritage_Categories() # 위치 기준으로 문화재 막대 그래프 그리기
    heritages_event()
    
if __name__ == '__main__':
    main()