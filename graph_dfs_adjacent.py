def solution(graph, start, end):
    stack = []
    result = []
    stack.append([start, [start]])
    while stack:
        node, path = stack.pop()
        if node == end:
            result.append(path)
        for subnode in set(graph[node]) - set(path):
            stack.append([subnode, path + [subnode]])
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

assert(solution(graph, 'A', 'F')) == [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
