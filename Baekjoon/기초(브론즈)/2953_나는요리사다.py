total = []

for i in range(5):
    scores = list(map(int, input().split()))
    total.append(sum(scores))

# 우승자의 인덱스+1 값, 우승자의 점수
print(total.index(max(total)) + 1, max(total))