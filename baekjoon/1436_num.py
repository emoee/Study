a = int(input())
list = []
if a > 1:
    for i in range(666, int(str(a)+"666")):
        test = str(i)
        if "666" in test:
            list.append(i)
    print(list[a-1])
else:
    print("666")