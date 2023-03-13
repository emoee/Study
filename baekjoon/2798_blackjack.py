n,m = map(int, input().split())
cards = list(map(int, input().split()))
summ = test = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                test= cards[i]+cards[j]+cards[k]
                if m >= test:
                    summ = max(summ,test)
print(summ)     