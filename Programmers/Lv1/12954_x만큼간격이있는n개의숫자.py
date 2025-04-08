def solution(x, n):
    answer = []
    for i in range(n):
        num = x * (i+1)
        answer.append(num)
        
    return answer