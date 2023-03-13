import sys
import math
n=246913
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

while 1:
    min = int(sys.stdin.readline())
    cnt = 0
    if min > 0:
        for i in primes:
            if min < i <= 2*min:
                cnt +=1
        print(cnt)
    else:
        break