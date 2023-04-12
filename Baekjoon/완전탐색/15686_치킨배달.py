from itertools import combinations

def total_sum(comb):
    value = 0
    for hx, hy in home:
        chicken_distance = 1e9
        # 가장 가까운 치킨거리 갱신
        for cx, cy in comb:
            chicken_distance = min(chicken_distance, abs(hx - cx) + abs(hy - cy))
        # 각 집의 치킨거리 누적
        value += chicken_distance
    return value

n, m = map(int, input().split())
home, chicken = [], []

for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] == 1:  # 집
            home.append((r, c))  
        elif temp[c] == 2:  # 치킨 집
            chicken.append((r, c))

# 치킨 집 중 m개의 치킨집을 보는 조합
comb_chicken = list(combinations(chicken, m))
result = 1e9

# 각 조합마다 치킨 거리의 합을 계산하는 함수
for comb in comb_chicken :
    result = min(result, total_sum(comb))

print(result)