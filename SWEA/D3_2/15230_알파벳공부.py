T = int(input())

for tc in range(1, T+1):
    N = int(input())
    incomes = list(map(int, input().split()))
    avg = sum(incomes) / N
    cnt = 0

    for i in incomes:
        if i <= avg:
            cnt += 1
    
    print(f'#{tc} {cnt}')