from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
import pandas as pd
import re

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def work(result):
    #검색 결과 개수 확인 및 설정
    URL = "https://www.worktogether.or.kr/empInfo/empInfoSrch/list/retriveWorkRegionEmpSrchList.do?pageIndex=1&pageUnit=10&relYn=N&totalEmpCount=0&jobsCount=0&len=0&tot=0&depth1SelCode=50000&depth2SelCode=50000&superCode=50000&ckWorkRegionCd=50000&mainSubYn=N&softMatchingPossibleYn=Y&disableEmpHopeGbn=Y,D&pageSize=10&firstIndex=1&lastIndex=1&recordCountPerPage=10&rowNo=0&region=50000&regionNm=%EC%A0%9C%EC%A3%BC&benefitSrchAndOr=O&serialversionuid=3990642507954558837&onlyContentSrchYn=N&softMatchingMinRate=+66&softMatchingMaxRate=100&empTpGbcd=1&charSet=EUC-KR&startPos=0&collectionName=tb_workinfo&payGbn=noPay&termSearchGbn=all&onlyTitleSrchYn=N&cloTermSearchGbn=all&resultCnt=10&sortOrderBy=DESC&sortField=DATE"
    driver.get(URL)
    driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page = re.sub(r"\s", "", soup.select_one('div > form > fieldset > span > strong').text)
    page = int(page)%10+1
    print(page)
    print(type(page))
    for i in range(1, page+1):
        URL = 'https://www.worktogether.or.kr/empInfo/empInfoSrch/list/retriveWorkRegionEmpSrchList.do?pageIndex={0}&pageUnit=10&relYn=N&totalEmpCount=0&jobsCount=0&len=0&tot=0&depth1SelCode=50000&depth2SelCode=50000&superCode=50000&ckWorkRegionCd=50000&mainSubYn=N&softMatchingPossibleYn=Y&disableEmpHopeGbn=Y,D&pageSize=10&firstIndex=1&lastIndex=1&recordCountPerPage=10&rowNo=0&region=50000&regionNm=%EC%A0%9C%EC%A3%BC&benefitSrchAndOr=O&serialversionuid=3990642507954558837&onlyContentSrchYn=N&softMatchingMinRate=+66&softMatchingMaxRate=100&empTpGbcd=1&charSet=EUC-KR&startPos=0&collectionName=tb_workinfo&payGbn=noPay&termSearchGbn=all&onlyTitleSrchYn=N&cloTermSearchGbn=all&resultCnt=10&sortOrderBy=DESC&sortField=DATE'.format(i)
        driver.get(URL)
        driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    
        list = soup.select('table.board_list > tbody > tr')
        print(len(list))
        for one in list: #기업하나씩
            company_name = one.select_one('td > a').text # 회사명
            company_work_name = one.select_one('td > p > a').text #공고명
            company = one.select('td > p > span')
            company_infoA = []
            for tag in company: # 급여 및 상여, 고용형태, 위치, 기간
                company_infoA.append(re.sub(r"\s", " ", tag.get_text()))
            company_infoB = []
            company = one.select('td > img')
            for tag in company: #신청 지원 안내, 장애인 채용 희망
                company_infoB.append(tag['alt'])
            
            result.append([company_name, company_work_name, company_infoA, company_infoB])
    
    driver.close()  
    
def main():
    result = []
    work(result)
    shoppingprint = pd.DataFrame(result, columns=('회사명', '공고명', '채용 상세 정보', '기타'))
    shoppingprint.to_csv('./jeju_worktogether/work.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    
if __name__ == '__main__':
    main()
