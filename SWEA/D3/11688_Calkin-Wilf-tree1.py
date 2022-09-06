T = int(input())

for tc in range(1, T+1):
    string = input()
    a = b = 1
    for i in string:
        if i == 'L':
            b += a
        if i == 'R':
            a += b
            
    print(f'#{tc} {a} {b}')