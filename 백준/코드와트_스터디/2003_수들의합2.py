n, m = map(int, input().split())
li = list(map(int, input().split()))

i, j, cnt, total = 0, 0, 0, 0

while(True):
    if total >= m:  # 수열의 합이 m보다 크거나 같다면
        total -= li[i]
        i += 1  # i 인덱스 증가
    elif j == n:  # j가 인덱스 범위 넘어가면 모두 순회한 상태
        break
    else:  # 수열의 합이 m보다 작은 경우
        total += li[j]
        j += 1  # j 인덱스 증가

    # i ~ j번째까지의 합이 m
    if total == m:
        cnt += 1

print(cnt)