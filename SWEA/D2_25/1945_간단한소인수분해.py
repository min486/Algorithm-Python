li = [2, 3, 5, 7, 11]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    li_cnt = [0] * len(li)

    for i in range(len(li)):
        while True:
            if n % li[i] == 0:
                li_cnt[i] += 1
                n //= li[i]
            else:
                break

    print(f'#{tc}', end=' ')
    print(*li_cnt)