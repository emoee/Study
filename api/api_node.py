import sys
from ast import literal_eval

sys.stdout = open('node_중구.txt', 'w')

with open('/Users/msun/Documents/apitest/nodelist.txt') as file:
    lines = file.readlines()
    dict = literal_eval(lines[0])
    for i in range(len(dict)):
        print(dict[i][int(str(dict[i].keys())[11:-2])]['wkt'][1:-1])
    
sys.stdout.close()
