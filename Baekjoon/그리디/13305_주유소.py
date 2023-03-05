n = int(input())
road_lens = list(map(int,input().split()))
prices = list(map(int,input().split()))

result = 0
now = prices[0]

for price, road_len in zip(prices, road_lens): # 가격과 거리를 하나씩 가져온다
    if now > price: # 현재 가격이 이제 도착한 주유소의 가격보다 비싸면
        now = price # 가격 갱신
    result += now * road_len # 계산

print(result)