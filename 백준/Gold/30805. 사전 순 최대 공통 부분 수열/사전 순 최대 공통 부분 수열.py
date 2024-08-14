n = int(input())
arr_A = list(map(int, input().split()))

m = int(input())
arr_B = list(map(int, input().split()))


def recur(arr_a, arr_b, result):
    if not arr_a or not arr_b:
        return result

    max_a = max(arr_a)
    max_b = max(arr_b)

    idx_a = arr_a.index(max_a)
    idx_b = arr_b.index(max_b)

    if max_a == max_b:
        result.append(max_a)
        return recur(arr_a[idx_a + 1:], arr_b[idx_b + 1:], result)
    elif max_a > max_b:
        arr_a.pop(idx_a)
        return recur(arr_a, arr_b, result)
    elif max_b > max_a:
        arr_b.pop(idx_b)
        return recur(arr_b, arr_a, result)


answer = recur(arr_A, arr_B, [])

print(len(answer))

if answer:
    print(*answer)