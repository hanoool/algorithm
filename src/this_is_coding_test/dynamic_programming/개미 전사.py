if __name__ == "__main__":
    n = int(input())
    storage = list(map(int, input().split()))
    dp = [0] * 101
    dp[1] = storage[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i-2]+storage[i-1], dp[i-1])
        
    print(dp[n])
    
# 해설
# n번째 식량창고까지 얻을 수 있는 최대 식량 개수는
# 1. n번째 식량창고 식량 개수 + n-2번째 식량창고까지 얻은 최대 개수
# 2. n-1번째 식량창고까지 얻은 최대 개수
# 중 큰 수이다.