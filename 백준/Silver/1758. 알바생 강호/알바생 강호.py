N = int(input())
tips = []
for i in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)
tip = 0
for i in range(len(tips)):
    result = tips[i] - i
    if result >= 0:
        tip += result

print(tip)