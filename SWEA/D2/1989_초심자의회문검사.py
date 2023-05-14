t = int(input())

for tc in range(1, t+1):
    li = input()
    
    if li == li[::-1]:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')