n = int(input())
data = list(map(int, input().split()))


def merge_arrays(a, b):
    res = []
    len_a, len_b = len(a), len(b)
    i, j = 0, 0
    for _ in range(len_a + len_b):
        if i < len_a and j < len_b:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        else:
            res.extend(a[i:] + b[j:])
            break

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    p = len(arr) // 2
    return merge_arrays(merge_sort(arr[:p]), merge_sort(arr[p:]))


print(*merge_sort(data))
