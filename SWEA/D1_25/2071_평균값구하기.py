t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))

    answer = round(sum(li) / len(li))

    print(f'#{tc} {answer}')