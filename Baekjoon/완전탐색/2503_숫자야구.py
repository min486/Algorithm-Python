from itertools import permutations
n = int(input())

# 1~9 중에 3개로 구성된 모든 경우
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
three = list(permutations(data, 3))

for _ in range(n):
    mh, s, b = map(int, input().split())
    mh = str(mh)
    remove_cnt = 0

    for i in range(len(three)):
        strike = ball = 0
        i -= remove_cnt  # three[0] 부터 시작

        for j in range(3):
            if three[i][j] == mh[j]:
                strike += 1
            elif mh[j] in three[i]:
                ball += 1
        
        # 제거 되면 제거 개수 증가
        # 다음 경우 확인할 때 index 위치 조정하기 위해
        if (strike != s) or (ball != b):  # 둘 중 하나라도 틀리면
            three.remove(three[i])
            remove_cnt += 1   

print(len(three))