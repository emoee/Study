# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    flyList = [0] * n
    for i in range(n):
        flyList[i] = list(map(int, input().split()))

    maxFly = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            currentFly = 0
            for x in range(m):
                for y in range(m):
                    currentFly += flyList[i + x][j + y]
            maxFly = max(maxFly, currentFly)

    print("#{} {}".format(test_case, maxFly))
    # ///////////////////////////////////////////////////////////////////////////////////
