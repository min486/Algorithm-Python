T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 'impossible'
    
    for i in range(2, 10):
        bs_n = N * i

        if len(str(N)) == len(str(bs_n)):
            if sorted(list(str(N))) == sorted(list(str(bs_n))):
                result = 'possible'
        else:
            break
    
    print(f'#{tc} {result}')