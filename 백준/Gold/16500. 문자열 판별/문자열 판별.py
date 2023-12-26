s = list(input())
n = int(input())

words = []
for _ in range(n):
    words.append(input())

dp = [0 for _ in range(len(s) + 1)]
dp[0] = 1

for i in range(len(s) + 1):
    for word in words:
        word_len = len(word)

        if i >= word_len and dp[i - word_len] == 1 and s[i - word_len:i] == list(word):
            dp[i] = 1

if dp[len(s)]:
    print(1)
else:
    print(0)