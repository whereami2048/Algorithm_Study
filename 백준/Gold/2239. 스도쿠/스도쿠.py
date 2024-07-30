sdoku = [list(map(int, input())) for _ in range(9)]

target_index = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            target_index.append((i, j))


def row_validate(x, num):
    for i in range(9):
        if sdoku[x][i] == num:
            return False

    return True


def col_validate(y, num):
    for i in range(9):
        if sdoku[i][y] == num:
            return False

    return True


def square_validate(x, y, num):
    start_x = x // 3 * 3
    start_y = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sdoku[start_x + i][start_y + j] == num:
                return False

    return True


def dfs(index):
    if index == len(target_index):
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j], end="")
            print()

        exit()

    x, y = target_index[index]

    for num in range(1, 10):
        if row_validate(x, num) and col_validate(y, num) and square_validate(x, y, num):
            sdoku[x][y] = num
            dfs(index + 1)
            sdoku[x][y] = 0


dfs(0)
