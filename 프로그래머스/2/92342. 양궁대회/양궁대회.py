from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    abs_score = 0;
    case1 = list(combinations_with_replacement(score, n))
    case2 = []

    for c in case1:
        s = [0 for _ in range(11)]
        for l in list(c):
            s[10-l] += 1
        case2.append(s)

    for c in case2:
        s1, s2 = 0, 0
        for i in range(11):
            if info[i] > 0 or c[i] > 0:
                if info[i] < c[i]:
                    s2 += 10-i
                else:
                    s1 += 10-i
        if s2 > s1:
            if (s2 - s1) > abs_score:
                abs_score = (s2 - s1)
                answer = [c]
            if (s2 - s1) == abs_score:
                answer.append(c)
    answer.sort(key=lambda x:(-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))     
    return answer[0] if len(answer) > 0 else [-1]