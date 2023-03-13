n = int(input())
xx = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))
    A = i + sum(num)
    if A == n:
        xx = i
        break
print(xx)