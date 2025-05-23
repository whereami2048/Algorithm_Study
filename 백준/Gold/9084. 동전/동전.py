T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    dp = [0 for _ in range(money + 1)]
    dp[0] = 1

    for coin in coins:
        for target in range(1, money + 1):
            if target >= coin:
                dp[target] += dp[target - coin]

    print(dp[money])