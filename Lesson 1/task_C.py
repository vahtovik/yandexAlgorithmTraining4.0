n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


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


print(*merge_arrays(arr1, arr2))
