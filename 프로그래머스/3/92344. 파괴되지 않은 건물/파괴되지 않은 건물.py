def solution(board, skill):
    n, m, cnt = len(board), len(board[0]), 0
    total_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for attak_type, y1, x1, y2, x2, degree in skill:
        val = -degree if attak_type == 1 else degree
        total_sum[y1][x1] += val
        total_sum[y2 + 1][x2 + 1] += val
        total_sum[y1][x2 + 1] -= val
        total_sum[y2 + 1][x1] -= val
    for i in range(n + 1):
        for j in range(m):
            total_sum[i][j + 1] += total_sum[i][j]
    for j in range(m + 1):
        for i in range(n):
            total_sum[i + 1][j] += total_sum[i][j]
            
    return sum([1 for i in range(n) for j in range(m) if board[i][j] + total_sum[i][j] > 0])