
import sys
import json

#sys.stdout = open('필요한것만.txt', 'w')

nodeList = []
check = ['107714', '107676', '107675', '107290', '252', '253', '254', '255', '256', '257', '107674', '258', '259', '107673', '262', '107672', '194033', '107154', '107155', '107176', '107177', '107178', '107460', '107455', '107456', '106906', '106907', '107129', '107076', '107075', '114849', '102592', '106939', '106859', '106860', '106861', '194044', '193725', '193726', '193727', '193728', '193729', '193730', '193731', '193733', '193734', '193738', '193992', '193993', '193994', '193995', '193996', '194018', '194025', '194027', '194028', '194029', '194030', '194031', '194034', '194035', '194036', '194037', '194039', '194040', '194041', '194043', '130105', '71798', '71797', '71796', '71795', '66722', '71821', '71822', '71823', '130106', '130138', '130139', '130140', '130144', '130145', '130148', '71820']
with open('/Users/msun/Documents/git/api/서초_강남.txt') as file:
    while True:
        Array = file.readline()
        Arraycheck = Array.split(",")
        lon = Arraycheck[1].split(" ")
        print(lon)
        #if(Arraycheck[0] in check):
            #print(lon[2])
            #print("%s, %s" %(lon[2],lon[1]),end="")
        if not Array: break
            
            
#print(nodeList)
#print(linkList)


#sys.stdout.close()

import sys

sys.stdout = open('nodecsv.txt', 'w')

with open('/Users/msun/Documents/git/필요한것만.txt') as file:
    while True:
        Array = file.readline()
        t = Array.split(" ")
        #if t[2] in "\n":
            
        print("{} ({}, {})".format(t[0], t[2][:-2], t[1][1:]))
        #if(Arraycheck[0] in check):
            #print(lon[2])
            #print("%s, %s" %(lon[2],lon[1]),end="")
        if not Array: break
            
            
#print(nodeList)
#print(linkList)


sys.stdout.close()
