#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    cnt = 0
    a = []
    for t in str(i):
        a.append(t)
    for j in range(0, len(a)):
        if (a[j] == "3" or a[j] == "6" or a[j] == "9"):
            cnt += 1
    if cnt !=0:
        print(int(cnt)*"-", end=" ")
    else:
        print(i, end=" ")