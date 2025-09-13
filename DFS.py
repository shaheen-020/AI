def dfs(graph, start):
    stack = [start]
    visited = set([start])
    result = []
    
    while stack:
        vertex = stack.pop()
        result.append(vertex)
        
        for neighbor in reversed (graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return result


if __name__ == "__main__":
    graph = {
       'A': ['B', 'C'],
       'B': ['D', 'E'],
       'C': ['F'],
       'D': [],
       'E': [],
       'F': []
    }
    print(dfs(graph , 'A'))