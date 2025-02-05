if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    
    dp = [10001] * (m + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(1, m + 1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
            
    if m != 10001:
        print(dp[m])
    else:
        print(-1)