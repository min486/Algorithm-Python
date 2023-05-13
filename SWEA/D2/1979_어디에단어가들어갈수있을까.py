t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    
    for i in range(n):
        leng = 0
        # 가로
        for j in range(n):
            if arr[i][j] == 1:
                leng += 1
            if arr[i][j] == 0 or j == n-1:
                if leng == k:
                    result += 1
                leng = 0
        # 세로
        for j in range(n):
            if arr[j][i] == 1:
                leng += 1
            if arr[j][i] == 0 or j == n-1:
                if leng == k:
                    result += 1
                leng = 0
                
    print(f'#{tc} {result}')