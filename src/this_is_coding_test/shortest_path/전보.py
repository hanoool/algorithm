import heapq
import sys
if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    
    n,m,c = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for i in range(1, m + 1):
        x, y, z = map(int, input().split())
        graph[x].append((y,z))
    
    def dijkstra(c):
        q = []
        heapq.heappush(q, (0, c))
        distance[c] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(c)
    
    count = 0
    max_distance = 0 # 도달 가능한 노드 중 가장 멀리있는 노드와의 최단거리
    for i in distance:
        if i != INF:
            count += 1
            max_distance = max(max_distance, i)
            
    print(count - 1, max_distance) # 시작 노드는 제외해야하므로 count - 1
    
    
    