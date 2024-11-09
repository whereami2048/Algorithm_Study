def convert_to_number(time):
    if ':' not in time:
        return int(time)
    
    a,b = time.split(':')
    
    return int(a) * 60 + int(b)

def solution(plans):
    p = []
    
    for title,start,time in plans:
        p.append((title, convert_to_number(start), convert_to_number(time)))
    
    p.sort(key=lambda x:x[1])
    ans = []
    stack = []
    for i in range(len(p)):
        if i == len(p)-1:
            ans.append(p[i][0])
            for i in range(-1, -len(stack)-1, -1):
                ans.append(stack[i][0])
            break
        extra = p[i+1][1] - (p[i][1]+p[i][2])
        
        if extra >= 0: 
            ans.append(p[i][0])
            while stack:
                if stack[-1][1] <= extra: 
                    k = stack.pop()
                    ans.append(k[0])
                    extra -= k[1]
                
                else:
                    stack[-1][1] -= extra
                    break
        else:
            stack.append([p[i][0], -extra])
    
    return ans