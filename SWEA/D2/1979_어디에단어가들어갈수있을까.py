T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(N):
        length = 0
        # 가로
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            if puzzle[i][j] == 0 or j == N-1:
                if length == K:
                    result += 1
                length = 0
        # 세로
        for j in range(N):
            if puzzle[j][i] == 1:
                length += 1
            if puzzle[j][i] == 0 or j == N-1:
                if length == K:
                    result += 1
                length = 0
                
    print(f'#{tc}', result)