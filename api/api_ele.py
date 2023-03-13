import sys
import json

sys.stdout = open('stdout.txt', 'w')

ElementaryList = []

with open('/Users/msun/Documents/apitest/서울시 초등학교 기본정보.json') as file:
    datas = json.load(file)
    jsonArray = datas.get('DATA')
    for value in jsonArray:
        if ('중구' in str(value.get('org_rdnma'))):
            Elementary = {value.get('schul_nm'), value.get('org_rdnma'), } 
            ElementaryList.append(Elementary)
            
print(ElementaryList)
sys.stdout.close()
