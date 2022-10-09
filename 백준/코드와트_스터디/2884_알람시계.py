h, m = map(int, input().split())

if m < 45:
    h -= 1
    if h < 0:  # h가 0 => -1
        h = 23
    m = 60 - 45 + m  # m = m + 15의 값
else :
    m -= 45
print(h, m)