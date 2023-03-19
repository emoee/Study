import pandas as pd
import requests
import sys
from ast import literal_eval

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



sys.stdout = open('nodestend.txt', 'w')

with open("/Users/msun/Documents/apitest/Elementarylist copy.txt","r") as f :
    lines = f.readlines()
    dict = literal_eval(lines[0])
    ele = []
    for i in range(len(dict)):
        ele.append(list(dict[i]))
    for value in ele:
        if('초등' not in str(value[1])):
            print("[{},{}]".format(value[0], get_coordinate(value[1])))
        else:
            print("[{},{}]".format(value[1], get_coordinate(value[0])))

sys.stdout.close()
f.close()