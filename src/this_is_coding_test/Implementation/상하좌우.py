if __name__ == "__main__":
    n = int(input())
    plans = list(input().split())
    dxy = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
    x,y = (1,1)
    for plan in plans:
        nx = x + dxy[plan][0]
        ny = y + dxy[plan][1]
        if nx <= 0 or ny <= 0 or nx > n or ny > n:
            continue
        else:
            x = nx
            y = ny
    print(x, y)