# pop(0)는 time complexity가 O(N)이므로 deque의 popleft를 활용한다
# 너비탐색은 옆으로 넓게 탐색하니 옆으로 늘어지는 큐를 사용한다고 기억하자
from collections import deque


def solution(graph, start_node):
    queue = deque()
    visit = []
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit


graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

assert solution(graph, 'A') == ['A', 'B', 'C', 'H', 'D', 'I', 'J', 'M', 'E', 'G', 'K', 'F', 'L']
