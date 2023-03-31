n = int(input())
li = []

for _ in range(n):
    s, e = map(int, input().split())
    li.append([s, e])

end, cnt = 0, 0

# 끝나는시간(e) 기준으로 오름차순 정렬, 같을 경우 시작시간(s) 기준으로 정렬
for s, e in sorted(li, key=lambda x : (x[1], x[0])):
    if end <= s:  # 전 회의의 끝나는시간 <= 현재 회의의 시작시간
        cnt += 1  # 회의 개수 +1
        end = e  # 끝나는 시간 갱신 

print(cnt)