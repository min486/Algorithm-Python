# 상 / 우 / 하 / 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solve(ci,cj,dr):
    cnt = 0  # 청소한 칸의 개수
    while True:  # 청소기가 움지이지 못할때 종료
        # 현재위치 청소
        arr[ci][cj] = 2
        cnt += 1

        # 왼쪽방향으로 순서대로 탐색해서 미청소 칸이면 이동/방향설정, 없으면 후진
        flag = True
        while flag:
            # 왼쪽부터 4방향중 미청소 칸 확인
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0:  # 미청소 칸이면
                    ci,cj,dr = ni,nj,nd
                    flag = False
                    break
            # 4방향 모두 미청소 칸 없으면 -> 후진
            else:
                bi, bj = ci-di[dr], cj-dj[dr]  # 후진할 위치
                if arr[bi][bj] == 1:  # 벽이면 종료
                    return cnt
                else:
                    ci,cj = bi,bj

N, M = map(int, input().split())
ci,cj,dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

res = solve(ci,cj,dr)
print(res)