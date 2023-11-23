import itertools


def get_distance(route, matrix):
    total = 0
    for i in range(len(route) - 1):
        total += matrix[route[i]][route[i + 1]]
    total += matrix[route[-1]][route[0]]
    return total


def traveling_salesman(cities_quantity, matrix):
    if cities_quantity == 1:
        return 0
    cities_routs = itertools.permutations(range(cities_quantity))
    min_distance = float('inf')
    for route in cities_routs:
        current_distance = get_distance(route, matrix)
        if current_distance < min_distance:
            min_distance = current_distance

    return min_distance if min_distance != float('inf') else -1


n = int(input())
matrix = [[num if num != 0 else float('inf') for num in map(int, input().split())] for _ in range(n)]

print(traveling_salesman(n, matrix))
