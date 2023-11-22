import heapq


def get_best_time(schedule, start, villages, current_time=0):
    time_to_arrive = {village: float('infinity') for village in villages}
    time_to_arrive[start] = current_time
    queue = [(current_time, start)]
    while queue:
        time_spent, current_village = heapq.heappop(queue)
        if time_spent > time_to_arrive[current_village]:
            continue
        if current_village in schedule:
            for village, time in schedule[current_village]:
                departure_time, arrival_time = time
                if departure_time < time_spent:
                    continue
                else:
                    if arrival_time < time_to_arrive[village]:
                        time_to_arrive[village] = arrival_time
                        heapq.heappush(queue, (arrival_time, village))

    return time_to_arrive


n = int(input())
d, v = map(int, input().split())
r = int(input())
schedule = {}
villages = set()

for _ in range(r):
    departure_village, departure_time, arrival_village, arrival_time = map(int, input().split())
    villages.add(departure_village)
    villages.add(arrival_village)
    schedule.setdefault(departure_village, []).append((arrival_village, (departure_time, arrival_time)))

res = get_best_time(schedule, d, villages)
print(res[v] if res[v] != float('infinity') else -1)
