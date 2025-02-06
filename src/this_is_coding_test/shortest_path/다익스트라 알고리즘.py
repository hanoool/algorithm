import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미 10억 설정
n, m = map(int(input().split())) # 노드, 간선 개수 입력 받기
start = int(input()) # 시작 노드 입력받기
graph = [[] for i in range [n +1]] # 각 노드에 연결되어 있는 노드 정보(노드 번호, 비용) 리스트
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기 - 노드에 연결되어 있는 노드 정보(노드 번호, 비용)
for _ in range(m):
    a,b,c = map(int, input().split()) # a노드에서 b노드 가는 비용 c
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])