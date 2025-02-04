def count_ways(S, coins):
    dp = [0] * (S + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, S + 1):
            dp[i] += dp[i - coin]

    return dp[S]


# Пример использования:
S = 4
coins = [1, 2, 3]
print(count_ways(S, coins))  # Вывод: 4