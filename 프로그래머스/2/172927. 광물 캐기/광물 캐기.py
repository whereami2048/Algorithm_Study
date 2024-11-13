def solution(picks, minerals):
    answer = 0
    mineralSort = []

    ableDigAmount = min(sum(picks) * 5, len(minerals))
    diaCnt, ironCnt, stoneCnt = 0, 0, 0

    for i in range(ableDigAmount):
        if minerals[i] == 'diamond':
            diaCnt += 1
        elif minerals[i] == 'iron':
            ironCnt += 1
        elif minerals[i] == 'stone':
            stoneCnt += 1
        
        if (i + 1) % 5 == 0 or i == ableDigAmount - 1:
            mineralSort.append((diaCnt, ironCnt, stoneCnt))
            diaCnt, ironCnt, stoneCnt = 0, 0, 0

    mineralSort.sort(key = lambda x : (x[0], x[1], x[2]), reverse = True)

    i = 0
    for diaCnt, ironCnt, stoneCnt in mineralSort:
        while picks[i] == 0:
            i += 1

        if i == 0:
            answer += (diaCnt + ironCnt + stoneCnt)
        elif i == 1:
            answer += (diaCnt * 5 + ironCnt + stoneCnt)
        elif i == 2:
            answer += (diaCnt * 25 + ironCnt * 5 + stoneCnt)

        picks[i] -= 1

    return answer