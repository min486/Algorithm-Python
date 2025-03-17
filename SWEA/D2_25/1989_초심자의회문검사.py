t = int(input())

for tc in range(1, t+1):
    text = input()
    
    if text == text[::-1]:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')