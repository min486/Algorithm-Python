def solution(alp, cop, problems):
    max_alp = max_cop = 0
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    return answer