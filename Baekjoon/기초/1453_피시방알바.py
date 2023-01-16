N = int(input())
seats = map(int, input().split())

# 전체 손님 수 - 중복된 숫자를 제외한 좌석 번호 수
result = N - len(set(seats))
print(result)