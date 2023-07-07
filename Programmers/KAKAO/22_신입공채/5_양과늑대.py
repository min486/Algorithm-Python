from collections import defaultdict

SHEEP = 0
WOLF = 1

def make_parent2children(edges):
    parent2children = defaultdict(list)
    for parent, child in edges:
        parent2children[parent].append(child)
    return parent2children

def max_sheep(nodes, parent2children, info, s, w):
    if not nodes:
        return s
    max_s = s
    for idx, node in enumerate(nodes):  # 현재 node를 탐색하지 않게 nodes에서 제거
        if info[node] == SHEEP:
            max_s = max(max_sheep(nodes[:idx] + nodes[idx+1:] + parent2children[node], parent2children, info, s+1, w), max_s)
        elif s > w + 1:  # 늑대인 경우, 양의 수가 늑대의 수보다 많아야 탐색 가능하므로
            max_s = max(max_sheep(nodes[:idx] + nodes[idx+1:] + parent2children[node], parent2children, info, s, w+1), max_s)
    return max_s

def solution(info, edges):
    parent2children = make_parent2children(edges)
    return max_sheep([0], parent2children, info, 0, 0)