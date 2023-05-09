t = int(input())

for tc in range(1, t+1):
    n, time, bbang = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    cnt = 0
    result = 'Possible'

    for t in li:
        cnt += 1
        if (t//time)*bbang < cnt:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')