from itertools import combinations
from functools import reduce
def solution(clothes):
    answer = 1
    wardrobe = {}
    
    for name, cloth_type in clothes:
        if wardrobe.get(cloth_type):
            wardrobe[cloth_type].append(name)
        else:
            wardrobe[cloth_type] = [name]
            
    for _, value in wardrobe.items():
        answer *= (len(value) + 1)
            
    return answer - 1