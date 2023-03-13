import sys
import json

sys.stdout = open('stdout.txt', 'w')

nodeList = []
linkList = []

with open('/Users/msun/Documents/apitest/서울시 자치구별 도보 네트워크 공간정보.json') as file:
    datas = json.load(file)

    jsonArray = datas.get('DATA')
    
    for value in jsonArray:
        if (value.get('node_id') != 0):
            nodeDict = { value.get('node_id') : {'wkt' : value.get('node_wkt'), 'link' : ' ' }} 
            nodeList.append(nodeDict)
            
            
        else:
            linkDict = { value.get('link_id') : {
                'startNode' : value.get('strt_node_id'),
                'endNode' : value.get('end_node_id') ,
                'len' : value.get('link_len')
                } }
            linkList.append(linkDict)
            
#print(nodeList)
print(linkList)


sys.stdout.close()
