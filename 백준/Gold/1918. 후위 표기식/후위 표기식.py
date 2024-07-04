import sys

input = sys.stdin.readline

original_expression = input()[:-1]

stack = []
result = ''
for char in original_expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(char)
    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(char)
    else:
        result += char

while stack:
    result += stack.pop()

print(result)