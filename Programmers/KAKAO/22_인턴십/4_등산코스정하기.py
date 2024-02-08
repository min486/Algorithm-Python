from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):

    # 그래프
    graph = defaultdict(set)
    for i, j, w in paths:
        graph[i].add((j, w))
        graph[j].add((i, w))

    # 무한대로 초기화
    intensities = [float('inf')] * (n + 1)  # 등산지점 1부터 시작
    heap = []
    for gate in gates:
        intensities[gate] = 0
        heappush(heap, (0, gate))

    while heap:
        i, n = heappop(heap)  # intensity와 노드 n
        if intensities[n] < i or n in summits:
            continue

        for j, ji in graph[n]:  # 이웃 노드와 이웃의 intensity 확인
            ni = max(i, ji)  # 이웃의 새로운 intensity
            if intensities[j] > ni:
                intensities[j] = ni
                heappush(heap, (ni, j))

    summits = set(summits)
    answer = [-1, float('inf')]
    for summit in sorted(summits):
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    return answer