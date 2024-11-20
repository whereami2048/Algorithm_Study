import re
from itertools import permutations

def solution(expression):
    result = []
    
    order_list = list(permutations(['*', '+', '-'], 3))
    for order in order_list:
        operands = list(map(int, re.split('[\*\+\-]', expression)))
        operators = [ch for ch in expression if ch in '*+-']

        for o in order:
            while o in operators:
                index = operators.index(o)

                if o == '*':
                    temp = operands[index] * operands[index + 1]
                elif o == '+':
                    temp = operands[index] + operands[index + 1]
                elif o == '-':
                    temp = operands[index] - operands[index + 1]

                operands[index] = temp
                operands.pop(index + 1)
                operators.pop(index)
        
        result.append(abs(operands[0]))
        
    return max(result)