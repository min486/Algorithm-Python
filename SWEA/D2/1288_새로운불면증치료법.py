import sys
sys.stdin = open("1288_input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    se = set()
    cnt = 0

    while len(se) < 10:
        cnt += 1
        num = n * cnt
        num_st = str(num)

        for i in range(len(num_st)):
            se.add(num_st[i])

    print(f'#{tc} {cnt*n}')