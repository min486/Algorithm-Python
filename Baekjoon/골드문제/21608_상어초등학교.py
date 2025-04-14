import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [[-1]*(N+2)] + [[-1]+[0]*N+[-1] for _ in range(N)] + [[-1]*(N+2)]
in_li = [list(map(int, input().split())) for _ in range(N*N)]
sorted_li = [[0]*5] + sorted(in_li)

# print(sorted_li)
pprint(sorted_li)