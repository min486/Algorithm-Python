T = int(input())

for tc in range(1, T + 1):
    ho1, mi1, ho2, mi2 = map(int, input().split())
    ho_total = ho1 + ho2
    mi_total = mi1 + mi2
    
    if mi_total > 59:
        ho_total += 1
        mi_total -= 60
        
    if ho_total > 12:
        ho_total -= 12
    
    print(f'#{tc} {ho_total} {mi_total}')