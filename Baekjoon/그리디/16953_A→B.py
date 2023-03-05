a, b = map(int, input().split())
cnt = 1  # 최솟값에 1을 더해야 해서

while True:
    # b가 a로 바뀌면 연산 끝
    if b == a:
        break
    # ((b가 2로 나누어 떨어지지 않음) and (b의 마지막 자리의 숫자가 1이 아님))
    # or (b가 a보다 작다면) 만들 수 없다
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        cnt = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1

print(cnt)