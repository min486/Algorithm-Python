# 범위가 100,000이므로 누적합을 사용하지 않고 구현하면
# 시간복잡도는 O(NM)이므로 1초 내에 불가능
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))
p_sum = [0]
temp = 0

for k in n_li:
    temp += k
    p_sum.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i-1])