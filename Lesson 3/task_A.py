import heapq


def dijkstra(matrix, start):
    distances = {vertex: float('infinity') for vertex, _ in enumerate(matrix[1:], start=1)}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in enumerate(matrix[current_vertex][1:], start=1):
            if weight <= 0:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


n, s, f = map(int, input().split())
matrix = [[0] * (n + 1)]

for _ in range(n):
    row = [0] + list(map(int, input().split()))
    matrix.append(row)

res = dijkstra(matrix, s)
print(-1 if res[f] == float('infinity') else res[f])
