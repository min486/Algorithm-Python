T = int(input())

for tc in range(1, T+1):
    S = input()
    if S.count('x') >= 8:
        result = 'NO'
    else:
        result = 'YES'

    print(f'#{tc} {result}')