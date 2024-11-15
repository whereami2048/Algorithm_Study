def solution(places):
    answer = []
    for room in places:
        if rules(room):
            answer.append(1)
        else:
            answer.append(0)
    return answer

#상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
#대각
dx_d = [1, 1, -1, -1]
dy_d = [1, -1, -1, 1]
    
def valid(X, Y):
    return (0 <= X <= 4) and (0 <=Y <= 4)

def rules(room):
    #조사가 필요한 자리 탐색
    check = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                check.append([i, j])

    for x, y in check:
        for i in range(4):
            #상하좌우에 P있는 경우 탐색
            X = x + dx[i]
            Y = y + dy[i]
            #상하좌우 건너에 P있으면서 사이에 파티션 없는 경우 탐색
            X1 = x + 2 * dx[i]
            Y1 = y + 2 * dy[i]
            #대각에 P있으면서 사이에 파티션 없는 경우 탐색
            X2 = x + dx_d[i]
            Y2 = y + dy_d[i]
            
            if valid(X, Y) and room[X][Y] == 'P': 
                return False
            if valid(X1, Y1) and room[X1][Y1] == 'P' and room[X][Y] != 'X':
                return False
            if valid(X2, Y2) and room[X2][Y2] == 'P' and (room[X2][y] != 'X' or room[x][Y2] != 'X'):
                return False

    return True