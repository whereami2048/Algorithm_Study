sequence1 = ['']
sequence2 = ['']
sequence1.extend(list(input()))
sequence2.extend(list(input()))

length1 = len(sequence1)
length2 = len(sequence2)

if length1 == 1 or length2 == 1:
    print(0)
    exit(0)

dp = [[0] * (length1 + 1) for _ in range(length2 + 1)]

for i in range(1, length2):
    for j in range(1, length1):
        if sequence2[i] == sequence1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[length2-1][length1-1])