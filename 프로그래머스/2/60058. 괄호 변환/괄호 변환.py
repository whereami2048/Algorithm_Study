def solution(p):
    def check_good(target):
        stack = []
        for t in target:
            if t == '(':
                stack.append(t)
            elif t == ')':
                if len(stack) == 0:
                    return False
                stack.pop()
        
        return True
    
    def divide(string):
        left_count, right_count = 0, 0
        for i in range(len(string)):
            if string[i] == '(':
                left_count += 1
            else:
                right_count += 1

            if left_count == right_count:
                return string[:i + 1], string[i + 1:]
            
    # 1.
    if len(p) == 0:
        return ''
    
    # 2.
    u, v = divide(p)

    # 3.
    if check_good(u):
        return u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = u[1:-1]
        for s in u:
            if s == '(':
                temp += ')'
            else:
                temp += '('
                
        return temp

