li = list(input())

stack = []
cnt = 0

for i in range(len(li)):
    if li[i] == '(':
        stack.append('(')
    else:
        # ( ) 레이저인 경우
        if li[i-1] == '(': 
            stack.pop()
            cnt += len(stack)
        # ) 닫히는 경우    
        else:
            stack.pop() 
            cnt += 1  # 막대기 남는 부분을 더해준다

print(cnt)