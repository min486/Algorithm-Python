import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    s = set()

    while (len(s) < 10):
        cnt += 1
        num = N * cnt
        nums = str(num)

        for i in range(len(nums)):
            s.add(nums[i])

    print(f'#{tc} {cnt*N}')



    
    

