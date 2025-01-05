def solution(clothes):
    # 옷을 종류별로 구분
    dic = {}
    for clothe, type in clothes:
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
        
    # 각 종류별로 입지 않는 경우를 추가하여 모든 조합 계산
    answer = 1
    for type in dic:   
        answer *= (dic[type] + 1)
    
    # 아무종류의 옷도 입지 않는 경우 제외
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))