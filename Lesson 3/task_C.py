import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        if current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                if weight <= 0:
                    continue
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances


n, k = map(int, input().split())
graph = {}

for _ in range(k):
    a, b, l = map(int, input().split())
    graph.setdefault(a, {})[b] = l
    graph.setdefault(b, {})[a] = l

start, finish = map(int, input().split())
res = dijkstra(graph, start)

if finish in res:
    print(-1 if res[finish] == float('infinity') else res[finish])
else:
    print(-1)
