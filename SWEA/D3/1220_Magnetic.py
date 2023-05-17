t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    t_arr = list(zip(*arr))  # 전치행렬 (열 -> 행)
    result = 0

    for li in t_arr:
        prev = 0
        for i in li:
            if i:
                if i == 2 and prev == 1:
                    result += 1
                prev = i
                
    print(f'#{tc} {result}')