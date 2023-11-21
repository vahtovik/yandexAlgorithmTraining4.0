import heapq


def dijkstra(matrix, start):
    distances = {vertex: [float('infinity'), 0] for vertex, _ in enumerate(matrix[1:], start=1)}
    distances[start][0] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex][0]:
            continue
        for neighbor, weight in enumerate(matrix[current_vertex][1:], start=1):
            if weight <= 0:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor][0]:
                distances[neighbor][0] = distance
                distances[neighbor][1] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances


n, s, f = map(int, input().split())
matrix = [[0] * (n + 1)]

for _ in range(n):
    row = [0] + list(map(int, input().split()))
    matrix.append(row)

res = dijkstra(matrix, s)
route = []
now = f

if res[f][0] != float('infinity'):
    while now != s:
        route.append(now)
        now = res[now][1]
    else:
        route.append(now)
    print(*reversed(route))
else:
    print(-1)
