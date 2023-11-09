import requests
import bs4
import pandas as pd

def lotto(result):
    for page in range(1000, 1069):
        lottonum = []
        URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=%d'%page
        raw = requests.get(URL)

        html = bs4.BeautifulSoup(raw.text,'html.parser')

        t = html.find('div',{'class':'nums'})

        luck_nums =t.find_all('span',{'class':'ball_645'})

        for num in luck_nums[:-1]:
            lottonum.append(int(num.text))
        luck = int(luck_nums[-1].text)
        result.append([page]+[lottonum]+[luck])
        
def main():
    result = []
    lotto(result)
    lottoprint = pd.DataFrame(result, columns=('회차', '당첨번호', '보너스번호'))
    lottoprint.to_csv('./lotto.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    
if __name__ == '__main__':
    main()