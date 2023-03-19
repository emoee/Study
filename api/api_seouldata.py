# 576a4f544e656c6935306f48764574
import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.Connect(host='localhost', port=3306, user='abb', password='abbpw', database='SeoulssgdateDB', charset='utf8')

cur = conn.cursor()
sql = "insert into Seouldata(stype, snode_id, snode_code,snode_wkt, slink_id, slink_code, slink_wkt, slink_len, sstartnode_id, sendnode_id, ssgg_cd, ssgg_nm, semd_cd, semd_nm) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
data =  ()

url = "http://openapi.seoul.go.kr:8088/키/xml/TbTraficWlkNet/1/5"

result = requests.get(url)
soup = BeautifulSoup(result.text, "lxml")
print(soup)
tbtraficwlknet = soup.find_all("row")
for row in tbtraficwlknet: #내가 원하는 데이터만 뽑은 거야
    stype = row.find('type').get_text()
    snode_id = row.find('node_id').get_text()
    snode_code = row.find('node_code').get_text()
    snode_wkt = row.find('node_wkt').get_text()
    slink_id = row.find('link_id').get_text()
    slink_code = row.find('link_code').get_text()
    slink_wkt = row.find('link_wkt').get_text()
    slink_len = row.find('link_len').get_text()
    sstartnode_id = row.find('strt_node_id').get_text()
    sendnode_id = row.find('end_node_id').get_text()
    ssgg_cd = row.find('sgg_cd').get_text()
    ssgg_nm = row.find('sgg_nm').get_text()
    semd_cd = row.find('emd_cd').get_text()
    semd_nm = row.find('emd_nm').get_text()
    data = (stype, snode_id, snode_code,snode_wkt, slink_id, slink_code, slink_wkt, slink_len, sstartnode_id, sendnode_id, ssgg_cd, ssgg_nm, semd_cd, semd_nm)
    cur.execute(sql, data)
conn.commit()
conn.close()