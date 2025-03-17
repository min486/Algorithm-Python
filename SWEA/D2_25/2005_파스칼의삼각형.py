t = int(input())

for tc in range(1, t+1):
    text = input()

    for i in range(1, 11):
        if text[:i] == text[i : i*2]:
            print(f'#{tc} {i}')
            break