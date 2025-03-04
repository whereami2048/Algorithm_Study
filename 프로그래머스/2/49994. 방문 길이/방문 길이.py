def solution(dirs):
    answer = 0
    
    road_history = []
    pos_x, pos_y = 0, 0
    for way in dirs:
        after_pos_x, after_pos_y, count = move(way, pos_x, pos_y)
        
        if not count:
            continue
        else:
            for history in road_history:
                if pos_x == history[0][0] and pos_y == history[0][1] and after_pos_x == history[1][0] and after_pos_y == history[1][1]:
                    break
                
                if after_pos_x == history[0][0] and after_pos_y == history[0][1] and pos_x == history[1][0] and pos_y == history[1][1]:
                    break
            else:
                answer += count
            
            road_history.append([(pos_x, pos_y), (after_pos_x, after_pos_y)])
            pos_x, pos_y = after_pos_x, after_pos_y
            
            
    return answer

def move(op, x, y):
    if op == 'U':
        if y + 1 <= 5:
            return x, y + 1, 1
    elif op == 'L':
        if x - 1 >= -5:
            return x - 1, y, 1
    elif op == 'R':
        if x + 1 <= 5:
            return x + 1, y, 1
    elif op == 'D':
        if y - 1 >= -5:
            return x, y - 1, 1
    
    return x, y, 0