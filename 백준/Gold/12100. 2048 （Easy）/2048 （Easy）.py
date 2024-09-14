import copy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def go_right(copy_board):
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if copy_board[i][j] != 0:
                temp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[i][pos] == 0:
                    copy_board[i][pos] = temp
                elif copy_board[i][pos] == temp:
                    copy_board[i][pos] += temp
                    pos -= 1
                else:
                    copy_board[i][pos - 1] = temp
                    pos -= 1

    return copy_board

def go_left(copy_board):
    for i in range(n):
        pos = 0
        for j in range(1, n):
            if copy_board[i][j] != 0:
                temp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[i][pos] == 0:
                    copy_board[i][pos] = temp
                elif copy_board[i][pos] == temp:
                    copy_board[i][pos] += temp
                    pos += 1
                else:
                    copy_board[i][pos + 1] = temp
                    pos += 1

    return copy_board

def go_up(copy_board):
    for j in range(n):
        pos = 0
        for i in range(n):
            if copy_board[i][j] != 0:
                temp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[pos][j] == 0:
                    copy_board[pos][j] = temp
                elif copy_board[pos][j] == temp:
                    copy_board[pos][j] += temp
                    pos += 1
                else:
                    copy_board[pos + 1][j] = temp
                    pos += 1

    return copy_board

def go_down(copy_board):
    for j in range(n):
        pos = n - 1
        for i in range(n-1, -1, -1):
            if copy_board[i][j] != 0:
                temp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[pos][j] == 0:
                    copy_board[pos][j] = temp
                elif copy_board[pos][j] == temp:
                    copy_board[pos][j] += temp
                    pos -= 1
                else:
                    copy_board[pos - 1][j] = temp
                    pos -= 1

    return copy_board

ans = 0
def dfs(cur, arr):
    global ans

    if cur == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(cur + 1, go_left(copy_arr))
        elif i == 1:
            dfs(cur + 1, go_right(copy_arr))
        elif i == 2:
            dfs(cur + 1, go_up(copy_arr))
        else:
            dfs(cur + 1, go_down(copy_arr))

dfs(0, board)

print(ans)
