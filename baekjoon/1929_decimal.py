import sys
import math

min, max = map(int,sys.stdin.readline().split())
for i in range(min, max+1):
    if i > 1:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
            print(i)