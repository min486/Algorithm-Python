t = int(input())

for tc in range(1, t+1):
    n = int(input())
    bus_stop = [0] * 5001

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_stop[i] += 1
            
    result = []
    p = int(input())

    for _ in range(p):
        stop_num = int(input())
        result.append(bus_stop[stop_num])

    print(f'#{tc}', *result)