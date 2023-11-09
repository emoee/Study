
#import sys
#sys.stdin = open("input.txt", "r")
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split(" ")))
    #print(prices)
    mprice = prices[N-1]
    benefit = 0
     
    for i in range(N-2, -1, -1):
        if prices[i] > mprice:
            mprice = prices[i]
        else:
            benefit += mprice - prices[i] 
       
    print("#{} {}".format(test_case, benefit))