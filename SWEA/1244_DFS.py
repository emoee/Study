def dfs(n):
    global result
    if n == time:
        result = max(result, int("".join(map(str, numbers))))
        return
     
    for i in range(origin_numbers_length-1):
        for j in range(i+1, origin_numbers_length):
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
            check = int("".join(map(str, numbers)))*10 + n
            if check not in test:
                dfs(n+1)
                test.append(check)
             
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
T = int(input())
for test_case in range(1, T+1):
    str_numbers, t = input().split()
    time = int(t)
    numbers = []
    for change in str_numbers:
        numbers.append(int(change))
    origin_numbers_length = len(str_numbers)
    result = 0
    test = []
    dfs(0)
    print(f"#{test_case} {result}")