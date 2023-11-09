from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import sys
import re

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def job(result, table_title, title):
    URL = 'https://www.kead.or.kr/bbs/ocredvbsns/bbsPage.do?menuId=MENU0633'
    driver.get(URL)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    title.append(soup.select_one('article > div.body.text > h3').text)
    title.append(re.sub(r"\s", "\t", soup.select_one('article > div.body.text > div > table > caption').text))
    
    
    table = soup.select('article > div.body.text > div.table > table > thead > tr > th')
    for ele in table:
        table_title.append(ele.get_text())
    
    table = soup.select('article > div.body.text > div.table > table > tbody > tr')
    time.sleep(1)
    for ele in table: #테이블
        detail = ele.select('td')
        table_content = []
        if len(detail) == 3:
                table_content.append("")
        for tag in detail: #행
            if "다운로드" in tag.text:
                break
            table_content.append(tag.text)
            if ele.select_one('td > a'):
                ele_url = ele.select_one('td > a')['href']  # Update ele_url value

        table_content.append(ele_url)
        result.append(table_content)
        
    
    
def main():
    result = []
    table_title = []
    title = []
    job(result, table_title, title)
    job_info_df = pd.DataFrame(result, columns=table_title)
    job_info_df.to_csv('./jeju_worktogether/job.csv', encoding='cp949', mode='w', index=True)
    
    sys.stdout = open('./jeju_worktogether/job_title.txt','w')
    print(title)
    
    del result[:]
    
if __name__ == '__main__':
    main()