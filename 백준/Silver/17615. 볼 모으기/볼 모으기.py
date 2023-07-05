import sys
N = int(input())
str = input()

cnt = sys.maxsize
def check_min(new_cnt):
    if cnt > new_cnt:
        return new_cnt
    else:
        return cnt

lRcase = str.lstrip('R')
cnt = check_min(lRcase.count('R'))
rRcase = str.rstrip('R')
cnt = check_min(rRcase.count('R'))
lLcase = str.lstrip('B')
cnt = check_min(lLcase.count('B'))
rLcase = str.rstrip('B')
cnt = check_min(rLcase.count('B'))

print(cnt)
