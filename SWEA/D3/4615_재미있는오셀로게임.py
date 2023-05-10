t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    # 초기 가운데 돌 배치
    mid = n // 2
    arr[mid][mid] = arr[mid+1][mid+1] = 2  # 백돌
    arr[mid][mid+1] = arr[mid+1][mid] = 1  # 흑돌

    for _ in range(m):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 탐색
        for di, dj in ((-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)):
            rev = []
            for mul in range(1, n):
                ni, nj = si + di * mul, sj + dj * mul
                # 범위 내 이면
                if 1 <= ni <= n and 1 <= nj <= n:
                    if arr[ni][nj] == 0:  # 돌 x
                        break
                    elif arr[ni][nj] == d:  # 같은 돌 이면
                        while rev:
                            ti,tj = rev.pop()
                            arr[ti][tj] = d
                        break
                    else:  # 다른 돌 이면
                        rev.append((ni, nj))
                else:
                    break

    b_cnt = w_cnt = 0
    for lst in arr:
        b_cnt += lst.count(1)
        w_cnt += lst.count(2)

    print(f'#{tc} {b_cnt} {w_cnt}')