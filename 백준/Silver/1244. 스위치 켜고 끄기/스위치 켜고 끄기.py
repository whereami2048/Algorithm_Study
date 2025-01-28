import sys
N = int(sys.stdin.readline())
switch = [-1] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

for _ in range(M):
    student, num = map(int, sys.stdin.readline().split())
    if student == 1 :
        for i in range(1, N//num+1):
            if switch[i*num] == 0 :
                switch[i*num] = 1
            else     :
                switch[i*num] = 0
    if student == 2 :
        if switch[num] == 0:
            switch[num] = 1
        else :
            switch[num] = 0
        left, right = num-1, num+1
        while left > 0 and right <= N and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1,1
            else :
                switch[left], switch[right] = 0,0
            left = left - 1
            right = right + 1

for k in range(1,N+1):
    print(switch[k], end=" ")
    if k % 20 == 0:
        print()