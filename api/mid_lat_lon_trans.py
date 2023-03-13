import pandas as pd
import json
import collections
from ast import literal_eval
with open("/Users/msun/Documents/apitest/nodelist copy.txt","r") as f :
    lines = f.readlines()
    dict = literal_eval(lines[0])
    
    for i in range(len(dict)):
        a,b = (dict[i][int(str(dict[i].keys())[11:-2])]['wkt'][6:-1].split(" "))
        dict[i][int(str(dict[i].keys())[11:-2])]['wkt'] = dict[i][int(str(dict[i].keys())[11:-2])]['wkt'].replace(dict[i][int(str(dict[i].keys())[11:-2])]['wkt'] , '(' + a + ',' + b +')')

    with open("/Users/msun/Documents/apitest/nodelist.txt","w") as f2 :
        f2.write(str(dict))
        f2.close()

f.close()
