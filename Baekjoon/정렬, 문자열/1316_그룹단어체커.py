N = int(input())
res = N

for _ in range(N):
    li = input()

    for i in range(len(li) - 1):
        if li[i] == li[i+1]:
            continue
        elif li[i] in li[i+2:]:
            res -= 1
            break

print(res)