from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import sys
import re

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def jobinfo(result, table_title):
    URL = 'https://hub.kead.or.kr/onlineEduRefeasyinfo.do'
    driver.get(URL)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    table = soup.select('table.tableB.type3.border.center > thead > tr > th')
    for ele in table:
        table_title.append(ele.text)
    table_title.append("url")
        
    table = soup.select('table.tableB.type3.border.center > tbody > tr')
    time.sleep(1)
    for ele in table: #테이블
        detail = ele.select('td')
        table_content = []
        cnt = 1
        for tag in detail: #행
            table_content.append(tag.text)
            if cnt == 1 and len(detail) == 3:
                table_content.append("")
                cnt = 0
            if ele.select_one('td > a'):
                eurl = ele.select_one('td > a')['onclick'].split("('")[1][:-2]  # Update ele_url value
                if len(eurl) == 1:
                    eurl = "0"+ eurl
                ele_url = "https://eduvod.kead.or.kr/VW/%s/01.html"%eurl

        table_content.append(ele_url)
        print(table_content)
        result.append(table_content)
        
def main():
    result = []
    table_title = []
    jobinfo(result, table_title)
    job_info_df = pd.DataFrame(result, columns=table_title)
    job_info_df.to_csv('./jeju_worktogether/jobinfo.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    
if __name__ == '__main__':
    main()