from itertools import combinations

t = int(input())

for tc in range(1, t+1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_score = 0
    
    for i in range(1, n+1):
        for com in combinations(arr, i):
            score = 0
            cal = 0
            for j in range(len(com)):
                score += com[j][0]
                cal += com[j][1]
            if cal > l:
                continue
            if max_score < score :
                max_score = score

    print(f'#{tc} {max_score}')