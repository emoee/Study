from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd

def crawl_yellow_kr():
    url = "http://yellow.kr/yhistoryl.jsp?level=0&view=1&period=0"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # CSS 선택자를 사용하여 원하는 요소를 찾습니다.
        target_table = soup.select("#featured > div.container > div.row > div > table > tbody:nth-child(2)")
        
        if target_table:
            rows = target_table[0].find_all("tr")
            data = []

            for row in rows:
                columns = row.find_all(["th", "td"])
                row_data = [col.get_text(strip=True).replace('\u0022', '') for col in columns]  # 큰따옴표 제거
                data.append(row_data)

            return data
        else:
            print("해당 테이블을 찾을 수 없습니다.")
            return None

def main():
    yellow_kr_data = crawl_yellow_kr()
    
    if yellow_kr_data:
        data = []
        for row in yellow_kr_data:
            if "* 날짜 : " not in row[1]:
                print(row)
    else:
        print("데이터를 추출할 수 없습니다.")

if __name__ == '__main__':
    main()
