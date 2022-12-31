n = int(input())
li = list(map(int, input().split()))
li.sort()  # 오름차순 정렬

result = 0  
person = 0  # 개인이 기다리는 시간

for i in li:
    person += i
    result += person

print(result)