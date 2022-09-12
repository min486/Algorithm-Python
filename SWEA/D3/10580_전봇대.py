T = int(input())

for tc in range(1, T+1):
    N = int(input())
    elec_all = []
    cnt = 0

    for _ in range(N):
        a, b = map(int, input().split())

        # 교차점 발생하는 경우 
        for el_a, el_b in elec_all:
            if a > el_a and b < el_b: # 기존선의 시작점보다 높으면, 기존선의 끝점보다 낮아야함
                cnt += 1
            elif a < el_a and b > el_b: # 기존선의 시작점보다 낮으면, 기존선의 끝점보다 높아야함
                cnt += 1

        elec_all.append([a, b])

    print(f'#{tc} {cnt}')