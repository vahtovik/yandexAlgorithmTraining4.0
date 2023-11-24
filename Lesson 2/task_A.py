s = input()
q = int(input())


def is_equal(from1, from2, slen):
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p
    )


n = len(s)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s

for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p

for _ in range(q):
    l, a, b = map(int, input().split())
    print('yes' if is_equal(a + 1, b + 1, l) else 'no')
