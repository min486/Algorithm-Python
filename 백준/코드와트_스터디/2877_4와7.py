k = int(input())
binary = format(k+1, 'b')  # 2진수 문자열로 변경
binary = binary[1:]  # 맨 앞자리 생략

# 0은 4로, 1은 7로 변경
print(binary.replace('0', '4').replace('1', '7'))