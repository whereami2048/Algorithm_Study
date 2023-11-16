n = int(input())

stack = []
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    while len(stack) > 0 and stack[-1] > y:
        ans += 1
        stack.pop()

    if len(stack) > 0 and stack[-1] == y:
        continue

    stack.append(y)

while len(stack) > 0:
    if stack.pop() > 0:
        ans += 1

print(ans)
