def solution(s):
    temp = sorted(list(map(int, s.split())))
    answer = f'{temp[0]} {temp[-1]}'
    return answer