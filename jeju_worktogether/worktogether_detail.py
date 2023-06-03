from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
import pandas as pd
import re
import sys
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def work(result, company_info, emp_info, company_title, emp_title):
    #검색 결과 개수 확인 및 설정
    URL = "https://www.worktogether.or.kr/empInfo/empInfoSrch/list/retriveWorkRegionEmpSrchList.do?pageIndex=1&pageUnit=10&relYn=N&totalEmpCount=0&jobsCount=0&len=0&tot=0&depth1SelCode=50000&depth2SelCode=50000&superCode=50000&ckWorkRegionCd=50000&mainSubYn=N&softMatchingPossibleYn=Y&disableEmpHopeGbn=Y,D&pageSize=10&firstIndex=1&lastIndex=1&recordCountPerPage=10&rowNo=0&region=50000&regionNm=%EC%A0%9C%EC%A3%BC&benefitSrchAndOr=O&serialversionuid=3990642507954558837&onlyContentSrchYn=N&softMatchingMinRate=+66&softMatchingMaxRate=100&empTpGbcd=1&charSet=EUC-KR&startPos=0&collectionName=tb_workinfo&payGbn=noPay&termSearchGbn=all&onlyTitleSrchYn=N&cloTermSearchGbn=all&resultCnt=10&sortOrderBy=DESC&sortField=DATE"
    driver.get(URL)
    driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page = re.sub(r"\s", "", soup.select_one('div > form > fieldset > span > strong').text)
    page = int(page)%10+1
    
    cnt = 1
    
    for i in range(1, page+1):
        URL = 'https://www.worktogether.or.kr/empInfo/empInfoSrch/list/retriveWorkRegionEmpSrchList.do?pageIndex={0}&pageUnit=10&relYn=N&totalEmpCount=0&jobsCount=0&len=0&tot=0&depth1SelCode=50000&depth2SelCode=50000&superCode=50000&ckWorkRegionCd=50000&mainSubYn=N&softMatchingPossibleYn=Y&disableEmpHopeGbn=Y,D&pageSize=10&firstIndex=1&lastIndex=1&recordCountPerPage=10&rowNo=0&region=50000&regionNm=%EC%A0%9C%EC%A3%BC&benefitSrchAndOr=O&serialversionuid=3990642507954558837&onlyContentSrchYn=N&softMatchingMinRate=+66&softMatchingMaxRate=100&empTpGbcd=1&charSet=EUC-KR&startPos=0&collectionName=tb_workinfo&payGbn=noPay&termSearchGbn=all&onlyTitleSrchYn=N&cloTermSearchGbn=all&resultCnt=10&sortOrderBy=DESC&sortField=DATE'.format(i)
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
                if i == 7:
                    break
                th_element = ele.select_one('th')
                td_element = ele.select_one('td')
                if th_element and td_element:
                    if cnt == 1:
                        company_title.append(re.sub(r"\s", "", th_element.get_text()))
                    companyi.append(re.sub(r"\s", "", td_element.get_text()))
                else:
                    if cnt == 1:
                        company_title.append("")
                    companyi.append("")

            company = soup1.select('div.empdetail > table > tbody > tr')
            for i, ele in enumerate(company):
                if i == 40:
                    break
                
                th_element = ele.select_one('th')
                td_element = ele.select_one('td')
                if th_element and td_element:
                    if cnt == 1:
                        emp_title.append(re.sub(r"\s", "", th_element.get_text()))
                    empi.append(re.sub(r"\s", "", td_element.get_text()))
                else:
                    if cnt == 1:
                        emp_title.append("")
                    empi.append("")
                    
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
    
    sys.stdout = open('output.txt','w')
    print(company_title)
    print(company_info)
    print("====")
    print(emp_title)
    print(emp_info)
    
    
    # workprint = pd.DataFrame(result, columns=('공고명', '회사명'))
    # workprint.to_csv('./jeju_worktogether/company.csv', encoding='cp949', mode='w', index=True)

    # workprint = pd.DataFrame(company_info, columns=company_title)
    # workprint.to_csv('./jeju_worktogether/company_info.csv', encoding='cp949', mode='w', index=True)

    # workprint = pd.DataFrame(emp_info, columns=emp_title)
    # workprint.to_csv('./jeju_worktogether/emp_info.csv', encoding='cp949', mode='w', index=True)
    
    workprint = pd.DataFrame(result, columns=['공고명', '회사명'])
    company_info_df = pd.DataFrame(company_info, columns=company_title)
    emp_info_df = pd.DataFrame(emp_info, columns=emp_title)

    combined_df = pd.concat([workprint, company_info_df, emp_info_df], axis=1)

    combined_df.to_csv('./jeju_worktogether/combined_data.csv', encoding='cp949', mode='w', index=False)

    del result[:]

if __name__ == '__main__':
    main()