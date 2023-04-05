n = int(input())
cnt = 0

for _ in range(n):
    stack = []
    word = list(input())

    for i in range(len(word)):
        # 스택 비어있거나 or 글자 다른 경우
        if not stack or stack[-1] != word[i]:
            stack.append(word[i])
        # 글자 같은 경우
        elif stack[-1] == word[i]:
            stack.pop()

    if not stack:
        cnt += 1

print(cnt)