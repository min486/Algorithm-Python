li = []
for a in range(1, 10):
    for b in range(1, 10):
        li.append(a*b)
all_li = list(set(li))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    if N in all_li:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')