import csv
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import folium


def company_show(label_length, image_width, image_height, title_font_size, label_font_size):
    encodings = ['utf-8', 'cp949', 'euc-kr'] 

    for encoding in encodings:
        try:
            with open("./combined_data.csv", encoding=encoding) as f:
                data = csv.reader(f)
                next(data)
                result = {}
                for row in data:
                    category = row[4]
                    result[category] = result.get(category, 0) + 1

                categories = list(result.keys())
                counts = list(result.values())

                truncated_categories = [category[:label_length] + '...' if len(category) > label_length else category for
                                        category in categories]

                sns.set_style('whitegrid')  # Set seaborn style
                plt.rc('font', family='AppleGothic')  # Mac 사용시 맑은 고딕은 한글깨짐 오류가 발생함.
                
                plt.figure(figsize=(image_width, image_height))
                plt.bar(truncated_categories, counts)
                plt.ylabel('Count', fontsize=label_font_size)
                plt.title('장애인 채용 회사 업종', fontsize=title_font_size)
                plt.xticks(rotation=90, fontsize=label_font_size)
                # plt.show()
                plt.savefig('./company.png')  # 이미지파일 저장

                break 
        except UnicodeDecodeError:
            continue 
    else:
        print("Unable to decode the file using any of the specified encodings.")

def disabled_access(label_length, title_font_size, label_font_size):
    encodings = ['utf-8', 'cp949', 'euc-kr'] 
    dash_count = 0 
    non_dash_count = 0 
    for encoding in encodings:
        try:
            with open("./combined_data.csv", encoding=encoding) as f:
                data = csv.reader(f)
                next(data)

                for row in data:
                    category = row[39]
                    if category == '-': #저장된 데이터가 없는 값이면 '-'이다.
                        dash_count += 1
                    else:
                        non_dash_count += 1

                sns.set_style('whitegrid')  # Set seaborn style
                plt.rc('font', family='AppleGothic')  # Mac 사용시 맑은 고딕은 한글깨짐 오류가 발생함.

                plt.figure() 
                
                _, _, autotexts = plt.pie([dash_count, non_dash_count], labels=['없다', '있다'], autopct='%1.1f%%')

                for autotext in autotexts:
                    autotext.set_fontsize(label_font_size)

                plt.title('장애인 편의시설 여부', fontsize=title_font_size)

                # plt.show()
                plt.savefig('./company_life_pie.png') 

                break 
        except UnicodeDecodeError:
            continue  
    else:
        print("Unable to decode the file using any of the specified encodings.")

def get_coordinate(address): # 주소를 입력받음
    result = "" 
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address # 카카오 api 서버스를 이용하여 접근
    rest_api_key = '4af578c58356b165193c3c4b7eafc1f0' # 사용자 api key
    header = {'Authorization': 'KakaoAK ' + rest_api_key} 

    r = requests.get(url, headers=header) 
 
    if r.status_code == 200: # 정보를 오류없이 받아왔다면
        if len(r.json()['documents']) != 0: # 길이가 0이 아니라면
            try : 
                result_address = r.json()["documents"][0]["address"]
                result = (result_address["y"],result_address["x"])  # 좌표 정보에 접근
            except:  # 예외처리
                print("오류1")
                
            
        else: # 길이가 0인경우 na처리
            print("오류2")
            
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    return result # 좌표를 반환

def location():
    encodings = ['utf-8', 'cp949', 'euc-kr'] 
    map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 초기 지도 중심 위치 설정
    for encoding in encodings:
        try:
            with open("./combined_data.csv", encoding=encoding) as f:
                data = csv.reader(f)
                next(data)
                result = {}
                for row in data:
                    category = row[31]
                    coordinate = get_coordinate(category)
                    
                    if isinstance(coordinate, tuple):
                        latitude, longitude = coordinate   
                        marker = folium.Marker(location=[latitude, longitude], popup=category)
                        marker.add_to(map)
                    else:
                        # 주소를 위도 경도로 변환할 수 없는 경우에 대한 예외 처리
                        continue
                
                map.save("map.html")       

                break 
        except UnicodeDecodeError:
            continue 
    else:
        print("Unable to decode the file using any of the specified encodings.")


def main():
    location()
    company_show(label_length=10, image_width=30, image_height=18, title_font_size=23, label_font_size=12)
    disabled_access(label_length=10, title_font_size=16, label_font_size=14)


if __name__ == '__main__':
    main()
