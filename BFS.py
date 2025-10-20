def bfs(graph, start):
    queue = [start]
    visited = set([start])
    result = []

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return result


if __name__ == "__main__":
    graph = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': ['f'],
        'd': [],
        'e': ['f'],
        'f': []
    }
    print(bfs(graph, 'a'))




