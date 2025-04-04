N = int(input())

numbers = sorted(list(map(int, input().split())))

if N < 3:
    print(0)
    exit(0)

count = 0

for i in range (N):
    left = 0
    right = N - 1
    target = numbers[i]
    while left < right:
        sum_numbers = numbers[left] + numbers[right]

        if sum_numbers == target:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                count += 1
                break
        elif sum_numbers < target:
            left += 1
        elif sum_numbers > target:
            right -= 1

print(count)