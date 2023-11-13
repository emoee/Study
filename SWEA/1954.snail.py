#import sys
#sys.stdin = open("input.txt", "r")
def printSnail(n):
    snail = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n-1, 0, n-1
        
    while (left <= right and top <= bottom):
        # top
        for index in range(left, right+1):
            snail[left][index] = num
            num += 1
        top += 1
            
        # right
        for index in range(top, bottom+1):
            snail[index][right] = num
            num += 1
        right -= 1
            
        # bottom 
        for index in range(right, left-1, -1):
            snail[bottom][index] = num
            num += 1
        bottom -= 1
            
        # left
        for index in range(bottom, top-1, -1):
            snail[index][left] = num
            num += 1
        left += 1
            
    # print
    for row in snail:
        print(" ".join(map(str, row)))

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    snail = int(input())
    maxSize = snail * snail
    print("#{}".format(test_case))
    printSnail(snail)
    # ///////////////////////////////////////////////////////////////////////////////////

    