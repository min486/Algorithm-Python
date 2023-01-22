n = int(input())

# 길의 각 높이, 오르막길 크기, 오르막길 크기들
road = list(map(int, input().split()))
road_size = 0
sizes = []

for i in range(n-1):
    if road[i] >= road[i+1]:
        road_size = 0
    else:
        road_size += (road[i+1] - road[i])
    sizes.append(road_size)

# 가장 큰 오르막길
print(max(sizes))