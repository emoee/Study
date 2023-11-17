#import sys
#sys.stdin = open("input.txt", "r")
    
def find_best_burger(idx, total_calories, current_taste, max_taste):
    global best_taste

    if total_calories > L:
        return

    if idx == N:
        best_taste = max(best_taste, current_taste)
        return

    find_best_burger(idx + 1, total_calories, current_taste, max_taste)
    find_best_burger(idx + 1, total_calories + ingredients[idx][1], current_taste + ingredients[idx][0], max_taste)


T = int(input())

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    best_taste = 0
    find_best_burger(0, 0, 0, best_taste)

    print(f"#{test_case} {best_taste}")
