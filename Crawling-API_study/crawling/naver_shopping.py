from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def shopping(result):
    URL = "https://search.shopping.naver.com/search/all?origQuery=%EC%83%A4%EC%9D%B8%EB%A8%B8%EC%8A%A4%EC%BC%93&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%83%A4%EC%9D%B8%EB%A8%B8%EC%8A%A4%EC%BC%93&sort=rel&timestamp=&viewType=list"
    driver.get(URL)
    driver.execute_script("window.scrollTo(0,3000);") #스크롤 아래로 내기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(1)
    goods = soup.select('div.product_item__MDtDF')
    time.sleep(2)
    for good in goods:
        item_name = good.select_one('div.product_title__Mmw2K > a').get('title')
        item_seller = good.select_one('div.product_mall_title__Xer1m > a').text
        item_price = good.select_one('span.price_num__S2p_v').text
        item_delivery = good.select_one('span.price_delivery__yw_We').text

        result.append([item_name, item_seller, item_price, item_delivery])
        
    driver.close()  
     
def main():
    result = []
    shopping(result)
    shoppingprint = pd.DataFrame(result, columns=('제품명', '판매자', '가격', '배송'))
    shoppingprint.to_csv('./shopping.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    
if __name__ == '__main__':
    main()

