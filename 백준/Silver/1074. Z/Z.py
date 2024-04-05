N, r, c = map(int, input().split())

def recur(n, r, c):
    if n == 0:
        return 0

    return 2 * (r % 2) + c % 2 + 4 * recur(n-1, r // 2, c // 2)

print(recur(N, r, c))