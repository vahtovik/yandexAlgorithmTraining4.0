a, b, c, d = map(int, input().split())


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_result(a, b, c, d):
    denominator = b * d
    numerator = a * d + c * b
    gcd = get_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


print(*get_result(a, b, c, d))
