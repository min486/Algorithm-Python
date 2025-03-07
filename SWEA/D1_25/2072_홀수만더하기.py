t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))

    answer = 0
    for i in li:
        if i % 2 == 1:
            answer += i

    print(f'#{tc} {answer}')