sugar = int(input())
count = 0

while sugar >= 0:
    if sugar%5 == 0:
        count += int(sugar//5)
        print(count)
        break
    sugar -= 3
    count += 1

if sugar < 0:
    print(-1)