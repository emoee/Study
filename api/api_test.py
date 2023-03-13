# 576a4f544e656c6935306f48764574

import requests
import bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

url = "http://openapi.seoul.go.kr:8088/576a4f544e656c6935306f48764574/xml/TbTraficWlkNet/1/5"

response = requests.get(url).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
