n = int(input())

if n == 1:
    print(0)
    exit(0)

is_prime = [2 for _ in range(n + 1)]
prime_numbers = []

for i in range(2, n + 1):
    if is_prime[i] == 0:
        continue
    elif is_prime[i] == 2:
        is_prime[i] = 1
        prime_numbers.append(i)
        temp = 2

        while(i * temp <= n):
            is_prime[i * temp] = 0
            temp += 1

left, right = 0, 0
prime_sum = prime_numbers[0]
count = 0

while(left <= right):
    if prime_sum > n:
        prime_sum -= prime_numbers[left]
        left += 1
    else:
        if prime_sum == n:
            count += 1

        right += 1

        if right == len(prime_numbers):
            break
            
        prime_sum += prime_numbers[right]

print(count)
