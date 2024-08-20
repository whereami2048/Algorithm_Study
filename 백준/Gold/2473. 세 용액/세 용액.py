import sys
input = sys.stdin.readline

n = int(input())

solution = sorted(list(map(int, input().split())))

result = []
temp_sum = sys.maxsize

for i in range(n-2):
    fix_num = solution[i]
    pos_left = i + 1
    pos_right = n - 1

    while pos_left < pos_right:
        cur_sum = solution[pos_left] + solution[pos_right] + fix_num

        if abs(cur_sum) < abs(temp_sum):
            temp_sum = cur_sum
            result = [fix_num, solution[pos_left], solution[pos_right]]
        elif cur_sum < 0:
            pos_left += 1
        elif cur_sum > 0:
            pos_right -= 1
        elif cur_sum == 0:
            print(*result)
            exit(0)


print(*result)
