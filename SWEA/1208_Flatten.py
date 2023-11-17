#import sys
#sys.stdin = open("input.txt", "r")
def dumps(numberList):
    maxIndex = 0
    minIndex = 0
    for j in range(len(numberList)):
        if numberList[maxIndex] < numberList[j]:
            maxIndex = j
        elif numberList[minIndex] > numberList[j]:
            minIndex = j
    return maxIndex, minIndex
    
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    numberList = list(map(int, input().split()))
    
    for i in range(n):
        maxIndex, minIndex = dumps(numberList)
        cha = numberList[maxIndex] - numberList[minIndex]
        if (cha != 0 or cha != 1):
            numberList[maxIndex] -= 1
            numberList[minIndex] += 1
        else:
            break
        
    maxIndex, minIndex = dumps(numberList)            
    cha = numberList[maxIndex] - numberList[minIndex]
    print("#{} {}".format(test_case, cha))