T = int(input())

for tc in range(1, T+1):
    num = input()
    if int(num[-1]) % 2 == 1:
        print(f'#{tc} Odd')
    else:
        print(f'#{tc} Even')