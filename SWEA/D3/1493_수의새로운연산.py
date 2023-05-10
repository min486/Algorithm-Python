y = [0] * 1001
x = [0] * 1001
x[1] = y[1] = 1
for i in range(2, 1000):
    y[i] = y[i - 1] + (i - 1)
    x[i] = x[i - 1] + i

T = int(input())
for tc in range(1, T + 1):
    p, q = map(int ,input().split())

    i, px, py = 1, 0, 0
    while i < 200:
        if y[i] <= p <= x[i]:
            diff = p - y[i]
            px, py = diff + 1, i - diff
            break
        i += 1
    #print(px, py)
    i, qx, qy = 1, 0, 0
    while i < 200:
        if y[i] <= q <= x[i]:
            diff = q - y[i]
            qx, qy = diff + 1, i - diff
            break
        i += 1
    #print(qx, qy)
    px, py = px + qx, py + qy

    print('#{} {}'.format(tc, y[py + px - 1] + px - 1))
###########################################################
L = 290 # 대략적인 삼각형 넓이로 가로세로 길이 만큼 생성 
lst = [1]*L
for i in range(2, L):
    lst[i] = lst[i-1]+i-1

def pos(n):
    si = 1
    while lst[si]<=n:
        si+=1
    d = n-lst[si-1]
    return si-1-d, d+1

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    pi, pj = pos(p)
    qi, qj = pos(q)
    si, sj = pi+qi, pj+qj
    ans = lst[si+sj-1]+sj-1
    print(f'#{test_case} {ans}')
#######################################
L = 500
lst = [1]*L
for i in range(2, L):
    lst[i] = lst[i-1]+i-1

def pos(n):
    si = 1
    while lst[si]<=n:
        si+=1
    d = n-lst[si-1]
    return si-1-d, d+1

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    pi, pj = pos(p)
    qi, qj = pos(q)
    si, sj = pi+qi, pj+qj
    ans = lst[si+sj-1]+sj-1
    print(f'#{test_case} {ans}')