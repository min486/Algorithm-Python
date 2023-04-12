target = int(input())
result = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
m = int(input())

if m: # 고장난게 있을 경우만 인풋을 받음
    broken = input().split()
else:
    broken = []

# 작은수에서 큰수 or 큰수에서 작은수로 이동하기 위한 범위
for num in range(1000001): 
    for button in str(num):
        if button in broken:  # 고장난 버튼이 있다면 스탑 후 다음 num으로 이동
            break
    # 번호를 눌러서 만들 수 있으면 (고장난 버튼 x)
    else:  
        # 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이
        result = min(result, len(str(num)) + abs(num - target)) 

print(result)