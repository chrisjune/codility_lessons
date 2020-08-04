def solution(graph, start, end):
    queue = []
    result = []
    queue.append([start, [start]])
    while queue:
        node, path = queue.pop(0)
        if node == end:
            result.append(path)
            print(path)
        for subnode in graph[node]:
            if subnode not in path:
                queue.append([subnode, path+[subnode]])
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

assert(solution(graph, 'A','F')) == [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]