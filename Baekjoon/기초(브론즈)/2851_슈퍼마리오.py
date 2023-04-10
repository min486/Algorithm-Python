result = 0

for i in range(10):
    score = int(input())
    result += score

    if result >= 100:
        # 100 - 전 점수의 합, 현재 점수의 합 - 100
        pre, now = 100 - (result - score), result - 100
        
        # 전 점수의 합이 100에 더 가까울 때
        if pre < now:
            result -= score
            break
        # 현 점수의 합이 100에 더 가까울 때 or 가까운 수 2개일 때
        elif pre > now or pre == now:
            break

print(result)