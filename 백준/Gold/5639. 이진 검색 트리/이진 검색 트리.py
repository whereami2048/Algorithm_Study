import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

numbers = []

while True:
    try:
        num = int(input())
        numbers.append(num)
    except:
        break


def recur(arr):
    if len(arr) == 0:
        return

    root = arr[0]
    arr_left, arr_right = [], []

    for i in range(1, len(arr)):
        if arr[i] > root:
            arr_left = arr[1:i]
            arr_right = arr[i:]
            break
    else:
        arr_left = arr[1:]

    recur(arr_left)
    recur(arr_right)

    print(root)


recur(numbers)
