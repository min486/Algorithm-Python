x, y = input().split()

# 슬라이싱을 이용해 뒤집고 int형 변환
rev_x = int(x[::-1])
rev_y = int(y[::-1])

# 합한 값을 뒤집기 위해 str형 변환
rev = str(rev_x + rev_y)

result = int((rev)[::-1])
print(result)