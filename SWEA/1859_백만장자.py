#import sys
#sys.stdin = open("input.txt", "r")
from collections import Counter
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())
    numbers = list(map(int, input().split()))
    score = Counter(numbers)
    
    max_score_count = max(score.values())
    #mode = max([score for score, count in score.items() if count == max_score_count])
    mode = 0
    for score, count in score.items():
        if count == max_score_count:
            if score > mode:
                mode = score
                
    print("#{} {}".format(number, mode))
    # ///////////////////////////////////////////////////////////////////////////////////
