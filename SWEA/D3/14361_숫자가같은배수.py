t = int(input())

for tc in range(1, t+1):
    n = int(input())
    result = 'impossible'
    
    for i in range(2, 11):
        n_bs = n * i

        if len(str(n)) == len(str(n_bs)):
            if sorted(str(n)) == sorted(str(n_bs)):
                result = 'possible'
        else:
            break
    
    print(f'#{tc} {result}')