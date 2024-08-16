n = int(input())

flowers = [tuple(map(int, input().split())) for _ in range(n)]

cur = (3, 1)
last = (11, 30)
count = 0

flowers.sort()
i = 0

while i < n:
    start_month, start_day, end_month, end_day = flowers[i]

    if (start_month, start_day) <= cur < (end_month, end_day):
        temp = (end_month, end_day)

        while i < n-1:
            temp_start_month, temp_start_day, temp_end_month, temp_end_day = flowers[i + 1]

            if cur < (temp_start_month, temp_start_day):
                break
            elif temp < (temp_end_month, temp_end_day):
                temp = (temp_end_month, temp_end_day)

            i += 1

        count += 1
        cur = temp

        if cur > last:
            print(count)
            exit(0)

    i += 1

print(0)