N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud_li = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]  # 구름 초기 위치

di, dj = [0,0,-1,-1,-1,0,1,1,1], [0,-1,-1,0,1,1,1,0,-1]
for _ in range(M):
    dir, dis = map(int, input().split())

    # 구름이동, 물증가, 구름사라짐
    cloud_li2 = []  # 이동할 구름의 위치 저장
    for ci,cj in cloud_li:
        ni, nj = (ci+di[dir]*dis+N) % N, (cj+dj[dir]*dis+N) % N
        arr[ni][nj] += 1
        cloud_li2.append((ni,nj))

    # 이동한 구름의 위치에서 대각선체크
    v = [[0]*N for _ in range(N)]
    for ci,cj in cloud_li2:
        v[ci][cj] = 1  # 구름위치 표시
        for dii,djj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ni, nj = ci+dii, cj+djj
            # 범위내, 물있으면
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                arr[ci][cj] += 1

    # 전체순회, 물>=2면 구름발생(물-=2), cloud_li2 위치 제외
    cloud_li = []
    for i in range(N):
        for j in range(N):
            # if arr[i][j] >= 2 and (i,j) not in cloud_li2:  # 500 ms
            if arr[i][j] >= 2 and v[i][j] == 0:
                arr[i][j] -= 2
                cloud_li.append((i,j))

res = 0
for li in arr:
    res += sum(li)
print(res)