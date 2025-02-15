if __name__ == "__main__":
    def dfs(i, j):
        global count
        if i < 0 or j < 0:
            return None
        if i >= n or j >= m:
            return None
        if visited[i][j] != 1 and map_info[i][j] != 1:
            visited[i][j] = 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
    
    n,m = map(int, input().split())
    map_info = []
    
    for i in range(n):
        map_info.append(list(map(int, input())))
        
    print(map_info)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    print(f"visited: {visited}")
    
    for i in range(len(map_info)):
        for j in map_info[i]:
            if visited[i][j] == 0 and map_info[i][j] == 0:
                dfs(i, j)
                count += 1
    print(count)
            