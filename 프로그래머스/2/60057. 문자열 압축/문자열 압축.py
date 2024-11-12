import sys

def solution(s):
    answer = sys.maxsize
    
    def compress(arr, chunk):
        tokens = []
        for i in range(0, len(arr), chunk):
            tokens.append(arr[i:i + chunk])
        
        index = 0
        result = ''
        while index < len(tokens):
            target_token = tokens[index]
            count = 0
            
            for pos in range(index, len(tokens)):
                if target_token != tokens[pos]:
                    break
                
                count += 1
                index = pos
            if count == 1:
                result += target_token
            else:
                result += f'{count}{target_token}'
                
            index += 1
        
        return len(result)
        
    for i in range(1, len(s) + 1):
        answer = min(answer, compress(s, i))
        
    return answer