from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    
    def check_equal(user_id, ban_id):
        if len(user_id) != len(ban_id):
            return False
        
        for i in range(len(ban_id)):
            if ban_id[i] == '*':
                continue
            elif ban_id[i] != user_id[i]:
                return False
        
        return True
    
    for target in permutations(user_id, len(banned_id)):
        is_answer = True
        
        for i in range(len(banned_id)):
            if not check_equal(target[i], banned_id[i]):
                is_answer = False
            
        if is_answer:
            if set(target) not in answer:
                answer.append(set(target))
    
    return len(answer)