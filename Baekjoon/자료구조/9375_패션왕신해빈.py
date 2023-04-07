tc = int(input())

for _ in range(tc):
    n = int(input())
    dic = {}

    for _ in range(n):
        dress = list(input().split())
        # 의상 종류별로 딕셔너리에 저장
        if dress[1] in dic:
            dic[dress[1]] += 1
        else:
            dic[dress[1]] = 2  # 입는 경우 + 안입는 경우
    
    result = 1
    for cnt in dic.values():
        result *= cnt  # 모든 경우의 수

    print(result - 1)  # 알몸인 경우의 수 1 빼기