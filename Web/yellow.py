from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd

def extract_date_period(text):
    # Find the index of "* 날짜 :"
    index = text.find("* 날짜 :")
    
    if index != -1:
        # Extract the date and period information
        date_info = text[:index].strip()
        period_info = text[index + len("* 날짜 :"):].strip()
        
        # Check if "~" is present in period_info
        if "~" in period_info:
            return date_info, period_info
        else:
            return date_info, 0
    else:
        # If "* 날짜 :" is not present, return None for period_info
        return text.strip(), 0

def date_split(date_string):
    date_parts = date_string.split("/")
    year = int(date_parts[0])
    month = int(date_parts[1]) if len(date_parts) > 1 else 0
    day = int(date_parts[2]) if len(date_parts) > 2 else 0
    return year, month, day

def classify_image(img_tag):
    if 'dull-blue-circle.png' in img_tag['src']:
        return 'w'
    elif 'dull-green-circle.png' in img_tag['src']:
        return 'k'
    else:
        return 0

def important_image(img_tag):
    if 'red-circle.png' in img_tag['src']:
        return 1
    else:
        return 0
    
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
                
                # 이미지 태그 추출
                img_tags = row.find_all('img')
                classification = classify_image(img_tags[0]) if img_tags else '0'
                important = important_image(img_tags[0]) if img_tags else '0'
                
                # row_data에 classification 추가
                row_data.append(classification)
                row_data.append(important)
                
                data.append(row_data)

            return data
        else:
            print("해당 테이블을 찾을 수 없습니다.")
            return None

def date_split(Hdate):
    if "/" in Hdate:
        sdate = Hdate.split("/")
        year = int(sdate[0]) if sdate[0].isdigit() else "check"
        month = int(sdate[1]) if len(sdate) > 1 and sdate[1].isdigit() else 0
        day = int(sdate[2]) if len(sdate) > 2 and sdate[2].isdigit() else 0
    elif "." in Hdate:
        sdate = Hdate.split(".")
        year = int(sdate[0]) if sdate[0].isdigit() else "check"
        month = int(sdate[1]) if len(sdate) > 1 and sdate[1].isdigit() else 0
        day = int(sdate[2]) if len(sdate) > 2 and sdate[2].isdigit() else 0
    else:
        # If neither "/" nor "." is present, it might be a single year or a non-numeric value
        year = int(Hdate) if Hdate.isdigit() else "check"
        month, day = 0, 0

    return year, month, day


def main():
    yellow_kr_data = crawl_yellow_kr()

    if yellow_kr_data:
        data = []

        # 두 개의 연속된 행을 처리하기 위해 인덱스를 2씩 증가시킵니다.
        for i in range(0, len(yellow_kr_data), 2):
            # 현재 행과 다음 행을 가져옵니다.
            row1 = yellow_kr_data[i]
            row2 = yellow_kr_data[i + 1] if i + 1 < len(yellow_kr_data) else [None] * len(row1)
            # 두 번째 행의 추가 정보와 기간 정보를 가져옵니다.
            additional_info2, period_info2 = extract_date_period(row2[1])
            year, month, day = date_split(row1[0])
            if "~" in row1[1] or "–" in row1[1]:
                row1[1] = row1[1].split("(")[0]
            
            # 첫 번째 행의 정보를 저장합니다.
            data.append([year, month, day, row1[1], additional_info2, period_info2, row1[2], row1[3]])

        # 수정된 데이터를 DataFrame으로 변환합니다.
        df = pd.DataFrame(data, columns=["year", "month", "day", "Hname", "detail", "date", "classify", "important"])

        # CSV 파일로 저장합니다 (quoting 옵션을 사용하여 큰따옴표 제외).
        df.to_csv('./Web/yellow_kr_data_f.csv', encoding='utf-8-sig', mode='w', index=False)

        print("데이터를 CSV 파일로 저장했습니다.")
    else:
        print("데이터를 추출할 수 없습니다.")


if __name__ == '__main__':
    main()
