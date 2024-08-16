n, k = map(int, input().split())

count = 0

while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    count += 2 ** idx
    n += 2 ** idx

print(count)
