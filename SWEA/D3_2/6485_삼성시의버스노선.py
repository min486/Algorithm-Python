t = int(input())

for tc in range(1, t+1):
    n = int(input())
    bus_line = [0] * 5001

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_line[i] += 1
    
    result = []
    p = int(input())
    for _ in range(p):
        bus_stop = int(input())
        result.append(bus_line[bus_stop])

    print(f'#{tc}', *result)