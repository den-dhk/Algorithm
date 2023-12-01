import heapq
INF = int(1e9)

def dijkstra(start, graph, distance, gates, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if i in gates:
                continue
            cost = i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for i in paths:
        a,b,c = i
        graph[a].append((b,c))
    
    # 다익스트라 함수 만들고 각 gates마다 summits으로 가는 함수 실행
    # 다익스트라 함수의 경우 intensity 최소인 경우로 만들기
    result = INF
    for start in gates:
        for end in summits:
            if result > dijkstra(start, graph, distance, gates, end):
                result = dijkstra(start, graph, distance, gates, end)
                answer = [end, result]
                
    return answer