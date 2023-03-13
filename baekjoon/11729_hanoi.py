def hanoiT(x,start, end):
    if x == 1:
        print(start, end)
        return
    hanoiT(x-1, start, 6-start-end)
    print(start, end)
    hanoiT(x-1, 6-start-end, end)

num = int(input())
print(2**num-1)
hanoiT(num, 1, 3) #세개의 장대
#다시 공부해보기