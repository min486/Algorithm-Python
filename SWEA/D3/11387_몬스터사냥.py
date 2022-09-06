T = int(input())

for tc in range(1, T+1):
    # D 데미지
    # L 공격의 레벨
    # N 때린 횟수
    D, L, N = map(int, input().split())
    total = 0
    
    for i in range(N):
        total += D * (1 + i * L * 0.01)
        
    print(f'#{tc} {int(total)}')