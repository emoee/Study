import sys
from ast import literal_eval
import time
import datetime

def Printfunction(cnt, f, a):
    if cnt == 1:
        print("{"+"{}:({},{})".format(dict[f[0]][1], dict[f[0]][2],dict[f[0]][3])+"}")
    else:
        node = "{}:".format(a)
        for n in range(len(f)):
            node = node + "({},{}),".format(dict[f[n]][2],dict[f[n]][3])
        print("{"+node[:-1]+"}")

start = time.time()
sys.stdout = open('nodestend.txt', 'w')

with open("/Users/msun/Documents/apitest/stdout copy.txt","r") as f :
    lines = f.readlines()
    dict = literal_eval(lines[0])
    for i in range(len(dict)):
        cnt = 0
        f = []
        for j in range(len(dict)):
            if dict[i][1] == dict[j][1]:
                #dict.append
                cnt += 1
                f.append(j)
        if cnt > 0:
            Printfunction(cnt,f,dict[i][1])
                               
sys.stdout.close()
end = time.time()
sec = (end - start)
result = datetime.timedelta(seconds=sec)
print(result)

