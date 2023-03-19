import requests
import json

listpolic = ["서울 서초구 주흥15길 41",
"서울 서초구 나루터로 38",
"서울 서초구 명달로 55",
"서울 서초구 염곡말길 9",
"서울 서초구 바우뫼로 45",
"서울 서초구 방배로 40",
""""서울 서초구 신반포로15길 14",
"서울 서초구 방배중앙로 131",
"서울 강남구 삼성로 761",
"서울 강남구 압구정로 33길 48",
""""서울 강남구 남부순환로378길29",
"서울 강남구 역삼로 117",
"서울 강남구 삼성로 236",
"서울 강남구 밤고개로 99"]

def get_coordinate(address): # 주소를 입력받음
    result = "" 
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address # 카카오 api 서버스를 이용하여 접근
    rest_api_key = '' # 사용자 api key
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

for j in range(len(listpolic)):
    print(get_coordinate(listpolic[j]))
