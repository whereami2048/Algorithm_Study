n = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(list(set(numbers)))

set_numbers = {sorted_numbers[i]: i for i in range(len(sorted_numbers))}

for num in numbers:
    print(set_numbers[num], end=" ")