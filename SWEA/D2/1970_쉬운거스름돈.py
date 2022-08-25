won_li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    for i in won_li:
        div = N // i
        N -= (i * div) 
        print(div, end = ' ')            
    print()