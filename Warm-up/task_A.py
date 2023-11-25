n, m = map(int, input().split())
data = list(map(int, input().split()))


def get_result(arr, a, b):
    minimum = min(arr[a: b + 1])
    for num in arr[a: b + 1]:
        if num > minimum:
            return num
    return 'NOT FOUND'


for _ in range(m):
    l, r = map(int, input().split())
    print(get_result(data, l, r))
