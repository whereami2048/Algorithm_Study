t = int(input())
for _ in range(t):
    command = input()
    n = int(input())

    numbers = list(input()[1:-1].split(','))
    if len(numbers) == 1 and numbers[0] == '':
        numbers = []
    else:
        numbers = list(map(int, numbers))

    is_pop_left = True
    pop_left_count = 0
    pop_right_count = 0
    r_count = 0

    for com in command:
        if com == 'R':
            r_count += 1
            is_pop_left = not is_pop_left
        else:
            if is_pop_left:
                pop_left_count += 1
            else:
                pop_right_count += 1

    if pop_left_count + pop_right_count > n:
        print('error')
    else:
        if r_count % 2 == 0:
            answer = ','.join(list(map(str, numbers[pop_left_count: n - pop_right_count])))
            print('[' + answer + ']')
        else:
            answer = ','.join(list(map(str, list(reversed(numbers[pop_left_count: n - pop_right_count])))))
            print('[' + answer + ']')
