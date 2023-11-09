#import sys
#sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    building = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    for i in range(2, building - 2):
        max_height = max(buildings[i - 2], buildings[i - 1], buildings[i + 1],buildings[i + 2])
        if buildings[i] > max_height:
            count += buildings[i] - max_height
    print("#{} {}".format(test_case, count))