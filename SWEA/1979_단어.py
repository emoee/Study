def count_word_spots(puzzle, N, K):
    count = 0
    for i in range(N):
        for j in range(N - K + 1):
            is_valid_spot = sum(puzzle[i][j + x] for x in range(K)) == K
            is_left_edge = j == 0 or puzzle[i][j - 1] == 0
            is_right_edge = j + K == N or puzzle[i][j + K] == 0

            if is_valid_spot and is_left_edge and is_right_edge:
                count += 1

    for i in range(N - K + 1):
        for j in range(N):
            is_valid_spot = sum(puzzle[i + x][j] for x in range(K)) == K
            is_top_edge = i == 0 or puzzle[i - 1][j] == 0
            is_bottom_edge = i + K == N or puzzle[i + K][j] == 0

            if is_valid_spot and is_top_edge and is_bottom_edge:
                count += 1
    return count

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = count_word_spots(puzzle, N, K)
    print("#{} {}".format(t, result))