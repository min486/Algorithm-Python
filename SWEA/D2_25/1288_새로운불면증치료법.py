t = int(input())

for tc in range(1, t+1):
    n = int(input())
    _set = set()
    cnt = 0

    while len(_set) < 10:
        cnt += 1
        num = n*cnt
        for i in str(num):
            _set.add(i)

    print(f'#{tc} {n*cnt}')