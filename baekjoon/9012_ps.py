import sys
num = int(input())

for i in range(num):
    cnt = 0
    lst = sys.stdin.readline()
    for j in lst:
        if '(' == j:
            cnt += 1
        elif ')' == j:
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")