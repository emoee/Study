import pandas as pd
import sys
from ast import literal_eval
sys.stdout = open('stdout.txt', 'w')
with open("/Users/msun/Documents/apitest/linklist copy.txt","r") as f :
    lines = f.readlines()
    dict = literal_eval(lines[0])
    dlist = []
    for i in range(len(dict)):
        dlist.append([int(str(dict[i].keys())[11:-2]), dict[i][int(str(dict[i].keys())[11:-2])]['startNode'],dict[i][int(str(dict[i].keys())[11:-2])]['endNode'], dict[i][int(str(dict[i].keys())[11:-2])]['len']])
    print(dlist)
f.close()    
sys.stdout.close()
    
'''
    for i in range(len(dict)):
        a,b = dict[i][int(str(dict[i].keys())[11:-2])]['startNode'], dict[i][int(str(dict[i].keys())[11:-2])]['endNode']
        dict[i][int(str(dict[i].keys())[11:-2])]['wkt'] = dict[i][int(str(dict[i].keys())[11:-2])]['wkt'].replace(dict[i][int(str(dict[i].keys())[11:-2])]['wkt'] , '(' + a + ',' + b +')')

    with open("/Users/msun/Documents/apitest/nodelist.txt","w") as f2 :
        f2.write(str(dict))
        f2.close()

f.close()
'''