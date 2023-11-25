from math import sqrt, atan2

x1, y1, x2, y2 = map(int, input().split())
radius1 = sqrt(x1 ** 2 + y1 ** 2)
radius2 = sqrt(x2 ** 2 + y2 ** 2)
closer = min(radius1, radius2)
further = max(radius1, radius2)

radian1 = atan2(y1, x1)
radian2 = atan2(y2, x2)

angle = abs(radian1 - radian2)
s = angle * closer + (further - closer)

res = min(abs(s), (radius1 + radius2))

print(res)
