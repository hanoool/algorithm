if __name__ == "__main__":
    n ,m = map(int, input().split())
    a, b, d = map(int, input().split())
    visited = [[0] * m for _ in range(n) ]
    visited[a][b] = 1
    map_info = []
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    def turn_left():
        global d
        if d == 0:
            d = 3
        else:
            d = d - 1

    for i in range(n):
        map_info.append(list(map(int, input().split())))
            
    turn_time = 0
    count = 1
    while True:
        turn_left()
        if map_info[a + dx[d]][b + dy[d]] == 0 and visited[a + dx[d]][b + dy[d]] == 0:
            a = a + dx[d]
            b = b + dy[d]
            visited[a][b] = 1
            turn_time = 0
            count += 1
            # continue
        else:
            turn_time += 1
            
        if turn_time == 4:
            turn_time = 0
            if map_info[a - dx[d]][b - dy[d]] == 0:
                a = a - dx[d]
                b = b - dy[d]
            else:
                break
            
    print(count)                
        


            
            