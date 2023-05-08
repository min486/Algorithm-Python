days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

T = int(input())

for tc in range(1, T+1):
    S = input()
    result = 0

    if days.index('SUN') == days.index(S):
        result = 7
    else:
        result = days.index('SUN') - days.index(S)

    print(f'#{tc} {result}')