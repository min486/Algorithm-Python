t = int(input())

for tc in range(1, t+1):
    li = input()

    for i in range(1, 10):
        if li[: i] == li[i : i*2]:
            print(f'#{tc} {i}')
            break