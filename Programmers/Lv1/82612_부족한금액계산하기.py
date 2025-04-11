def solution(price, money, count):
    total = 0  # 총 이용금액
    for i in range(1, count+1):
        total += price*i
    
    # 금액 모자라는 경우
    if money < total:
        return total - money
    else:
        return 0