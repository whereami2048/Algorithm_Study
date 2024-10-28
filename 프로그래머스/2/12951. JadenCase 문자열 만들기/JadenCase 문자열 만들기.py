# def solution(s):
#     return " ".join([word[0].upper() + word[1:].lower() if word else word for word in s.split(" ")])

def solution(s):
    check = s.split(' ')
    
    for i in range(len(check)):
        check[i] = check[i].capitalize()
        
    return ' '.join(check)