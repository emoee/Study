num = int(input())
list = []
for i in range(num):
    test = int(input())
    if test > 0:
        list.append(test)
    else:
        list.pop()

print(sum(list))