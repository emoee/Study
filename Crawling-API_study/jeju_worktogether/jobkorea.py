from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
import pandas as pd
import re
import sys
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def korea(result, company_title):
    count = 1
    count2 = 1
    count3 = 1
    for page in range(1, 5):
        URL = "https://www.jobkorea.co.kr/search/?stext=장애인&pref=2&tabType=recruit&Page_No=%d&Ord=ExactDesc&focusTab=&focusGno=41735875"%page
        driver.get(URL)
        driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        list = soup.select('div.list-default > ul.clear > li')
        for i, one in enumerate(list): #기업하나씩
            if i < 20:
                companyi = []
                if count == 1:
                    company_title.append("공고명")
                    company_title.append("기업명")
                    
                company_URL = one.select_one('div.post > div > a').attrs['href']
                script = f"window.open('{company_URL}');"
                driver.execute_script(script)
                driver.switch_to.window(driver.window_handles[1])  
                driver.get_window_position(driver.window_handles[1])
                time.sleep(1)
                
                driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
                soup1 = BeautifulSoup(driver.page_source, 'html.parser')
                time.sleep(1)
                
                companyi.append(re.sub(r"\s", " ",one.select_one('div.post > div.post-list-info > a').text).strip())
                companyi.append(re.sub(r"\s", "", soup1.select_one('article.artReadJobSum > div.sumTit > h3 > div.header > span').text))
                
                companybig = soup1.select('div.tbRow.clear > div.tbCol')
                
                for i, ele in enumerate(companybig):
                    if i == 0:
                        
                        company = ele.select('dl > dt')
                        for i, j in enumerate(company):
                            if count == 1 and i < 3:
                                company_title.append(j.text) #  지원자격 타이틀
                
                        company = ele.select('dl > dd')
                        for i, j in enumerate(company):
                            companyi.append(re.sub(r"\s", " ", j.text).strip()) #  지원자격 내용
                            if i == 2 :
                                break
                    
                    if i == 1:
                        company = ele.select('dl > dt')
                        for i, j in enumerate(company):
                            if count2 == 1 and len(company) == 4:
                                company_title.append(j.text) #  지원자격 타이틀                                
                            if count2 == 1 and len(company) == 4 and i == 3:
                                count2 = 0
                                
                        company = ele.select('dl > dt, dl > dd')
                        pairs = [company[i:i+2] for i in range(0, len(company), 2)]

                        while len(pairs) < 4:
                            pairs.append(['', ''])  # Fill with empty pairs until it reaches four

                        for pair in pairs[:4]:  # Save only the first four pairs
                            dt = pair[0]
                            dd = pair[1]
                            dd_text = dd.text.strip() if dd else "내용없음"
                            companyi.append(re.sub(r"\s", " ", dd_text).strip())
                    else:
                        continue
                company = soup1.select('article.artReadPeriod > div > dl.date > dt')
                if len(company) == 2:        
                    if count3 == 1:
                        for ele in company:
                            company_title.append(ele.text) #  날짜 타이틀
                    count = 0
                    count3 = 0
                    
                company = soup1.select('article.artReadPeriod > div > dl.date > dd')
                if len(company) == 2:
                    for ele in company:
                        companyi.append(ele.text) #  날짜 내용
                else:
                    companyi.append("상시채용")
                    companyi.append("상시채용")

                result.append(companyi)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
            elif i == 20:
                break

    driver.close()  

def main():
    result = []
    company_title = []
    korea(result, company_title)
    print(company_title)
    job_korea_df = pd.DataFrame(result, columns=company_title)
    job_korea_df.to_csv('./jeju_worktogether/jobkorea.csv', encoding='cp949', mode='w', index=True)
    
    del result[:]

if __name__ == '__main__':
    main()