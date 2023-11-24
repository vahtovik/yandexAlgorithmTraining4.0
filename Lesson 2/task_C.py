def z_function(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

    return z


string = input()
print(*z_function(string))
