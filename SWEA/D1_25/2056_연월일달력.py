li = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def check(m, d):
    if 1 <= m <= 12:
        if 1 <= d <= li[m]:
            return True
        else:
            return False
    else:
        return False

t = int(input())

for tc in range(1, t+1):
    text = input()

    year = text[:4]
    month = text[4:6]
    day = text[6:]

    print(f'#{tc}', end=' ')

    if check(int(month), int(day)):
        print(year, month, day, sep='/')
    else:
        print(-1)