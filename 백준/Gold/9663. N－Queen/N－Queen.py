n = int(input())

count = 0
row = [0 for _ in range(n)]


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def dfs(x):
    global count
    
    if x == n:
        count += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)


dfs(0)

print(count)