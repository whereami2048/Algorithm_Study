target_str = input()
bomb_str = input()

bomb_str_length = len(bomb_str)

stack = []

for i in range(len(target_str)):
    stack.append(target_str[i])
    if ''.join(stack[-bomb_str_length:]) == bomb_str:
        for _ in range(bomb_str_length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
