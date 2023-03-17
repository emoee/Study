import sys
from ast import literal_eval

sys.stdout = open('/Users/msun/Documents/git/api/안전비상벨위치정보.csv', 'r')

with open('/Users/msun/Documents/git/api/안전비상벨위치정보.csv') as file:
    lines = file.readlines()
    dict = literal_eval(lines[0])
    for i in range(len(dict)):
        print(dict[i][int(str(dict[i].keys())[11:-2])]['wkt'][1:-1])
    
sys.stdout.close()
