day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

def check(m, d):
    if 1 <= m <= 12:
        if 1 <= d <= day_list[m]:
            return True
        else:
            return False
    else:
        return False

t = int(input())

for tc in range(1, t+1):
    li = input()
    year = li[0 : 4]
    month = li[4 : 6]
    day = li[6 :]

    print(f'#{tc}', end=' ')

    if check(int(month), int(day)):
        print(year, month, day, sep='/')
    else:
        print('-1')