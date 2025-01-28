string = input() + ' '

new_string = ''
stack = []
is_blank = False

for char in string:
    if char == '<':
        is_blank = True
        for _ in range(len(stack)):
            new_string += stack.pop()

    stack.append(char)

    if char == '>':
        is_blank = False
        for _ in range(len(stack)):
            new_string += stack.pop(0)

    if not is_blank and char == ' ':
        stack.pop()
        for _ in range(len(stack)):
            new_string += stack.pop()
        new_string += ' '

print(new_string)