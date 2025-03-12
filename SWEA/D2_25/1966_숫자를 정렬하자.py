t = int(input())

for tc in range(1, t+1):
    n = input()
    li = list(map(int, input().split()))
    li.sort()

    print(f'#{tc}', *li)