t = int(input())

for tc in range(1, t+1):
    print(f'#{tc}')
    n = int(input())
    
    for i in range(n):
        print(' '.join(str(11**i)))