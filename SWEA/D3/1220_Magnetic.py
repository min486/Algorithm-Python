t = 10

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    t_graph = list(zip(*graph))  # 전치행렬 (열 -> 행)

    for li in t_graph:
        prev = 0
        for i in li:
            if i:
                if i == 2 and prev == 1:
                    result += 1
                prev = i
                
    print(f'#{tc} {result}')