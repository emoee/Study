n = int(input())
kc = []
rank = []
for i in range(n):
    kc.append(tuple(map(int, input().split(" "))))
    rank.append(1)

for j in range(n):
    for k in range(n):
        if kc[j][0]> kc[k][0] and kc[j][1] > kc[k][1]:
            rank[k] += 1

print(*rank)