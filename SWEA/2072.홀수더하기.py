#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number_list = list(map(int, input().split(" ")))
    total = 0
    for i in number_list:
        if i%2 == 1:
            total += i
    
    print("#{} {}".format(test_case, total))
         
    # ///////////////////////////////////////////////////////////////////////////////////
