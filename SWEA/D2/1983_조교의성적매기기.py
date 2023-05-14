grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    div = n // 10
    total_li = [] 
    
    for _ in range(n):
        score, score2, score3 = map(int, input().split())
        total = score*0.35 + score2*0.45 + score3*0.2
        total_li.append(total)           
        
    K_total = total_li[k-1]
    total_li.sort(reverse = True)
    K_rank = total_li.index(K_total) // div
        
    print(f'#{tc}', grade[K_rank])