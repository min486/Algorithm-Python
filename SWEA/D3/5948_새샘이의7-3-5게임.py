from itertools import combinations

t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    se = set()  
    for i in combinations(li, 3):
        se.add(sum(i))  # 합이 같을 수 있으므로 중복제거
    result = sorted(list(se))

    print(f'#{tc} {result[-5]}')