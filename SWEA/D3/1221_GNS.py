info = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())

for tc in range(1, t+1):
    _ = input().split()
    li = list(input().split())

    for i in range(len(li)):
        li[i] = info.index(li[i])
    
    li.sort()
    for i in range(len(li)):
        li[i] = info[li[i]]

    print(f'#{tc}')
    print(*li)