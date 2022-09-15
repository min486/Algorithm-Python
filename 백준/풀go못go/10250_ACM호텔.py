T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    result = 0

    if n % h != 0:
        result = (n % h) * 100 + (n // h) + 1
    else:
        result = h * 100 + (n // h)

    print(result)