def solution(alp, cop, problems):
    max_alp = max_cop = 0

    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    
    times = [[float('inf') for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    
    # 알고력과 코딩력이 100인데 문제가 필요한건 10일때 인덱스 에러
    # 가지고 있는 알고력과 코딩럭이 더 클 경우 대비
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    times[alp][cop] = 0
    
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a + 1 <= max_alp:
                # 다른 방법이랑 비교하기 위해 min() 사용
                times[a+1][c] = min(times[a+1][c], times[a][c] + 1)
            if c + 1 <= max_cop:
                times[a][c+1] = min(times[a][c+1], times[a][c] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    # 10 -> 15, max_alp : 13 경우 min()으로 대비
                    na, nc = min(a + alp_rwd, max_alp), min(c + cop_rwd, max_cop)
                    times[na][nc] = min(times[na][nc], times[a][c] + cost)
                
    return times[-1][-1]