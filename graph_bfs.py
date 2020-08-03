# pop(0)은 O(N)
# collection 의 deque를 사용하면 O(1)
# 너비로 넓히기 때문에 queue를 사용한다고 기억하하자

from collections import deque
def solution(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


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
