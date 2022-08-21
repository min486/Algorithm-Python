T = int(input())
 
day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
 
def check(x, y):
    if 1<= x <= 12:
        if 1 <= y <= day_list[x]:
            return True
        else:
            return False
 
for tc in range(1, T + 1):
    li = input()
    year = li[0 : 4]
    month = li[4 : 6]
    day = li[6 :]
     
    print(f'#{tc}', end = ' ')
    if check(int(month), int(day)):
        print(year, month, day, sep = '/')
    else:
        print('-1')