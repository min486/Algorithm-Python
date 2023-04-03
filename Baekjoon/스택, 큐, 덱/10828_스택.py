# 시간초과 나서 sys.stdin.readline 사용
import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        li.append(int(order[1]))
    elif order[0] == 'pop':
        if li:
            print(li.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(li))
    elif order[0] == 'empty':
        if li:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if li:
            print(li[-1])
        else:
            print(-1)