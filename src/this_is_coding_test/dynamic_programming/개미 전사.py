if __name__ == "__main__":
    n = int(input())
    storage = list(map(int, input().split()))
    
    d = [0] * 101
    d[1] = storage[0]
    d[2] = storage[1]
    for i in range(3, n + 1):
        d[i] = max(d[i-1], d[i-2]+ storage[i-1])
        
    print(d[n])
        
    