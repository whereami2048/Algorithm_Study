target = int(input())
ans = abs(100 - target)
broken_number_count = int(input())
if broken_number_count:
    broken_numbers = set(input().split())
else:
    broken_numbers = set()

for num in range(1000001):
    for N in str(num):
        if N in broken_numbers:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)
