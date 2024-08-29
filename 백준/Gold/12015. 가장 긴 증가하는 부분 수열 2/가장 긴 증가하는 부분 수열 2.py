import bisect

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

for i in arr:
    if result[-1] < i:
        result.append(i)
    else:
        index = bisect.bisect_left(result, i)
        result[index] = i

print(len(result))