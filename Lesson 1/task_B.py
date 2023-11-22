import random

n = int(input())
data = list(map(int, input().split()))


def quick_sort(arr):
    if len(arr) > 1:
        x = random.choice(arr)
        less = [e for e in arr if e < x]
        equal = [e for e in arr if e == x]
        greater = [e for e in arr if e > x]
        return quick_sort(less) + equal + quick_sort(greater)

    return arr


print(*quick_sort(data))
