t = int(input())

for tc in range(1, t+1):
    print(f'#{tc}')
    n = int(input())
    li = []

    for _ in range(n):
        alpha, num = input().split()
        for _ in range(int(num)):
            li.append(alpha)

    cnt = 0
    for i in range(len(li)):
        print(li[i], end='')
        cnt += 1

        if cnt == 10:
            cnt = 0
            print()
    print()