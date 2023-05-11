t = 10

for tc in range(1, t+1):
    _, li = input().split()
    stack = []

    for i in range(len(li)):
        if stack and stack[-1] == li[i]:
            stack.pop()
        else:
            stack.append(li[i])

    result = ''.join(stack)
    print(f'#{tc} {result}')