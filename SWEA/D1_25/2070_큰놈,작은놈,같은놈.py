t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())

    if a > b:
        answer = '>'
    elif a < b:
        answer = '<'
    elif a == b:
        answer = '='

    print(f'#{tc} {answer}')