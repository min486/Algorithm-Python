T = int(input())

for tc in range(T):
    r, s = input().split()
    
    for i in s:
        print(int(r) * i, end='')
    print()