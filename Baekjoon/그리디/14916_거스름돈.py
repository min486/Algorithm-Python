n = int(input())
rem = n % 5  # n을 5로 나눈 나머지

if n == 1 or n == 3:
    print(-1)
elif rem % 2 == 0:
    print(n // 5 + rem // 2)
# 나머지가 2로 나누어 떨어지지 않는 경우
else:
    print((n // 5) - 1 + (rem + 5) // 2)