n1, n2 = map(int, input().split())
ants1 = list(input())
ants2 = list(input())
t = int(input())

ants1.reverse()  # 그룹1 진행 방향 변경
group = ants1 + ants2  # ['C', 'B', 'A', 'D', 'E', 'F']

# 그룹1 전진, 그룹2 뛰어넘기
for _ in range(t):
    # 반복문을 통해 두 개미 그룹을 확인
    for i in range(len(group) - 1):
        # 두 개미 그룹이 만나면 위치 변경
        if group[i] in ants1 and group[i + 1] in ants2:
            group[i], group[i + 1] = group[i + 1], group[i]

            # 위치를 바꾼 개미가 선두개미이면 반복 탈출 
            # 왼쪽 그룹의 선두개미가 오른쪽 그룹과 마주 보게 되어 교환하면
            if group[i + 1] == ants1[-1]:
                break

print("".join(group))