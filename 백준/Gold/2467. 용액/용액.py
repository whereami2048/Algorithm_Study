N = int(input())

x, y = 0, 0
left = 0
right = N - 1

value = float("inf")

solutions = [int(x) for x in input().split()]

while left < right:
    current = solutions[left] + solutions[right]

    if abs(current) <= value:
        x = solutions[left]
        y = solutions[right]
        value = abs(current)

    if current <= 0:
        left += 1
    else:
        right -= 1


print(x, y)