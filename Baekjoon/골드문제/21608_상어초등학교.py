import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[-1]*(n+2)] + [[-1]+[0]*n+[-1] for _ in range(n)] + [[-1]*(n+2)]
inp_li = [list(map(int, input().split())) for _ in range(n*n)]
sort_li = [[0]*5] + sorted(inp_li)

# pprint(sort_li)

# [1] 전체 순회하면서 좋아하는 학생 수, 빈칸 수 체크
for li in inp_li:
    mx = empty_mx = -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > 0:  # 빈칸 아니면 패스
                continue
            cnt = empty_cnt = 0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i+di, j+dj
                if arr[ni][nj] in li:  # 좋아하는 친구인 경우
                    cnt += 1
                if arr[ni][nj] == 0:  # 빈칸인 경우
                    empty_cnt += 1
            if mx<cnt or (mx==cnt and empty_mx<empty_cnt):
                mx, empty_mx = cnt, empty_cnt
                ei, ej = i, j
    arr[ei][ej] = li[0]

# [2] 각 학생의 만족도의 총합
tbl = [0, 1, 10, 100, 1000]
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt = 0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i+di, j+dj
            if arr[ni][nj] in sort_li[arr[i][j]]:
                cnt += 1
        ans += tbl[cnt]
print(ans)