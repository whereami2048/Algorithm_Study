import copy

t = int(input())

for _ in range(t):
    answer = []
    N, M = map(int, input().split())
    important = [(index, val) for index, val in enumerate(list(map(int, input().split())))]

    count = 0
    max_importance = max(important, key=lambda x: x[1])[1]
    copy_important = copy.deepcopy(important)

    while copy_important:
        if copy_important[0][1] == max_importance:
            pop_val = copy_important.pop(0)
            answer.append(pop_val)
            if copy_important:
                max_importance = max(copy_important, key=lambda x: x[1])[1]
        else:
            first_num = copy_important.pop(0)
            copy_important.append(first_num)

    for index, val in enumerate(answer):
        if val[0] == M:
            print(index + 1)
