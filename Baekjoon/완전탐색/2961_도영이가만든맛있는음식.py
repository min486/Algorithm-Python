from itertools import combinations

n = int(input())
foods = [list(map(int, input().split())) for _ in range(n)]
result = 1000000000

# 재료 개수별(1~n개) 조합
for comb in [combinations(foods, i) for i in range(1,n+1)]:
    # 재료 개수에 해당하는 모든 경우
    for co in comb:
        sin, ssn = 1, 0  
        # 경우마다 신맛, 쓴맛 비교
        for si, ss in co:
            sin *= si 
            ssn += ss
        # 최소값 갱신, 차이를 구하기 위해 절댓값으로
        result = min(result, abs(sin - ssn))

print(result)