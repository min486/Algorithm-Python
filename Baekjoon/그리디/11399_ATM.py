n = int(input())
time_li = list(map(int, input().split()))

# 시간의 합을 최소로 만들기 위해 오름차순 정렬
time_li.sort()
result = 0  
person = 0  # 개인이 기다리는 시간

for i in time_li:
    person += i
    result += person

print(result)