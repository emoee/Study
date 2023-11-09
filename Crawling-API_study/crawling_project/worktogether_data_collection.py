from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
import pandas as pd
import re
import sys
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def work(result, company_info, emp_info, company_title, emp_title):
    cnt = 1
    for page in range(1, 15):
        URL = "https://www.worktogether.or.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?pageIndex=%d&pageUnit=10&relYn=N&totalEmpCount=0&jobsCount=0&len=0&tot=0&mainSubYn=N&softMatchingPossibleYn=N&preferentialGbn=D&disableEmpHopeGbn=D&pageSize=10&firstIndex=1&lastIndex=1&recordCountPerPage=10&rowNo=0&benefitSrchAndOr=O&serialversionuid=3990642507954558837&onlyContentSrchYn=N&softMatchingMinRate=+66&softMatchingMaxRate=100&softMatchingYn=N&empTpGbcd=1&charSet=EUC-KR&startPos=0&collectionName=tb_workinfo&certifiYn=N&preferentialYn=Y&preferential=D&siteClcd=WORK&majorYn=N&onlyTitleSrchYn=N&keywordWantedTitle=N&keywordBusiNm=N&keywordJobCont=N&keywordStaAreaNm=N&keywordSecd=N|N|N|N&resultCnt=10&sortOrderBy=DESC&sortField=DATE&tabMode=1"%page
        driver.get(URL)
        driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        list = soup.select('table.board_list > tbody > tr')
        
        for one in list: #기업하나씩
            empi = []
            companyi = []
            
            company_URL = one.select_one('td > a').attrs['href']
            script = f"window.open('{company_URL}');"
            driver.execute_script(script)
            driver.switch_to.window(driver.window_handles[1])  
            driver.get_window_position(driver.window_handles[1])
            time.sleep(1)
            
            driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
            soup1 = BeautifulSoup(driver.page_source, 'html.parser')
            time.sleep(1)
            
            title = soup1.select_one('div.company-detail > div.leftBox > p').text
            name = soup1.select_one('div.company-tit > p').text
             
            company = soup1.select('div.detail-table > table > tbody > tr')
            for i, ele in  enumerate(company):
                if i == 5:
                    break
                th_element = ele.select_one('th')
                td_element = ele.select_one('td')
                if th_element and td_element:
                    if cnt ==1 and th_element.text not in company_title:
                        company_title.append(re.sub(r"\s", "", th_element.get_text()))
                    companyi.append(re.sub(r"\s", "", td_element.get_text()))

            print(len(company_title))
            print(len(companyi))
            
            company = soup1.select('div.empdetail > table > tbody > tr')
            for i, ele in enumerate(company):
                if i == 33:
                    break
                
                th_element = ele.select_one('th')
                td_element = ele.select_one('td')
                if th_element and td_element:
                    if cnt == 1 and th_element.text not in emp_title:
                        emp_title.append(re.sub(r"\s", "", th_element.get_text()))
                    empi.append(re.sub(r"\s", "", td_element.get_text()))

                    
            print(len(emp_title))
            print(len(empi))  
            cnt += 1
            result.append([title, name])
            emp_info.append(empi)
            company_info.append(companyi)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)

    driver.close()  

def main():
    result = []
    emp_info = []
    company_info = []
    company_title = []
    emp_title = []
    work(result, company_info, emp_info, company_title, emp_title)
    
    workprint = pd.DataFrame(result, columns=['공고명', '회사명'])
    company_info_df = pd.DataFrame(company_info, columns=company_title)
    emp_info_df = pd.DataFrame(emp_info, columns=emp_title)

    combined_df = pd.concat([workprint, company_info_df, emp_info_df], axis=1)
    combined_df.to_csv('./combined_data.csv', encoding='utf-8', mode='w', index=False)
    # combined_df.to_csv('./combined_data.csv', encoding='euc-kr', mode='w', index=False) 오류
    # combined_df.to_csv('./combined_data.csv', encoding='cp949', mode='w', index=False) 오류

    del result[:]

if __name__ == '__main__':
    main()