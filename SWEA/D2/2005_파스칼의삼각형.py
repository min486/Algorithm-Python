T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    
    for i in range(N):
        print(' '.join(str(11 ** i)))