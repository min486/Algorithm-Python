grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    div = N // 10
    total_list = [] 
    
    for _ in range(N):
        mid, final, home = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + home * 0.2
        total_list.append(total)           
        
    K_total = total_list[K-1]
    total_list.sort(reverse = True)
    K_rank = total_list.index(K_total) // div
        
    print(f'#{tc}', grade[K_rank])