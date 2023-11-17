#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    numberList = list(map(int, input().split()))
    sum = 0;
    for i in range(len(numberList)):
        sum += numberList[i]
    avg = round(sum/len(numberList))
    print("#{} {}".format(test_case, avg))
    # ///////////////////////////////////////////////////////////////////////////////////
