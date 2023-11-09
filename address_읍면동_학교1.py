import pandas as pd
import requests

def search_address(query):
    api_url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {'Authorization': 'KakaoAK {}'.format(APP_KEY)}
    params = {
        "query": query
    }
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()

    if data.get("documents"):
        address = data["documents"][0]["address_name"]
        x = data["documents"][0]["x"]
        y = data["documents"][0]["y"]
        return address, x, y
    else:
        return None

# CSV 파일에서 주소 불러오기
df = pd.read_csv("/Users/msun/Documents/Crawling-API_study_git/제주특별자치도교육청_학교현황_20221001.csv", encoding="EUC-KR")
APP_KEY = '4af578c58356b165193c3c4b7eafc1f0'
# 주소 검색 및 결과 저장할 리스트 초기화
results = []

# 주소 검색
for index, row in df.iterrows():
    query = row[7]
    result = search_address(query)
    
    if result:
        address, x, y = result
        result_dict = {
            "Original Address": query,
            "Searched Address": address,
            "Longitude": x,
            "Latitude": y
        }
        results.append(result_dict)

# 결과를 DataFrame으로 변환
result_df = pd.DataFrame(results)

# 결과를 CSV 파일로 저장
result_df.to_csv("address_results.csv", index=False)
