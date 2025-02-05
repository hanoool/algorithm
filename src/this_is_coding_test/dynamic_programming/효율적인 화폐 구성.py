if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    dp = [10001] * (m + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(1, m + 1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    
    if dp[m] != 10001:
        print(dp[m])
    else:
        print(-1)
    
# 해설
# [x,y,z] 화폐가 있는 가운데, m원을 만들기 위해서는 
# 1. [x,y,z]로 m-x원을 만드는 화폐 최소 개수
# 2. [x,y,z]로 m-y원을 만드는 화폐 최소 개수
# 3. [x,y,z]로 m-z원을 만드는 화폐 최소 개수
# 중 최소 값에 1을 더하면 됨
