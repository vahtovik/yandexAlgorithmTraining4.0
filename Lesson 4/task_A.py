n = int(input())
initial_arr = list(range(1, n + 1))


def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return None
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr


while initial_arr is not None:
    print(''.join(map(str, initial_arr)))
    initial_arr = next_permutation(initial_arr)
