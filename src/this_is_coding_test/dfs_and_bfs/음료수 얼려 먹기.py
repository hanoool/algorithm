if __name__ == "__main__":
    def dfs(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        if map_info[i][j] != 1:
            map_info[i][j] = 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            return True
        return False
    
    n,m = map(int, input().split())
    map_info = []
    
    for i in range(n):
        map_info.append(list(map(int, input())))
        
    count = 0
    
    for i in range(len(map_info)):
        for j in map_info[i]:
            if dfs(i, j) == True:
                count += 1
    print(count)
            