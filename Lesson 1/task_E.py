n = int(input())
data = [input() for _ in range(n)]
phases = len(data[0])
d = {i: {k: [0, []] for k in range(10)} for i in range(1, phases + 1)}

print('Initial array:')
print(', '.join(data))
print('**********')

for p in range(1, phases + 1):
    print(f'Phase {p}')

    for i in range(n):
        nm, num = data[i][-p], data[i]
        d[p][int(nm)][0] += 1
        d[p][int(nm)][1].append(num)

    for j in d[p]:
        r = d[p][j][1]
        print(f'Bucket {j}: {", ".join(r) if r else "empty"}')

    data = []
    for k, v in d[p].items():
        if v[0] > 0:
            data.extend(v[1])

    print('**********')

print('Sorted array:')
print(', '.join(data))
