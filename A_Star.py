import heapq

def a_star_search(graph, start, goal, h):
    frontier = [(0 + h[start], start, [start], 0)]
    explored = set()

    while frontier:
        f, node, path, g = heapq.heappop(frontier)

        if node == goal:
            return path, g

        if node in explored:
            continue
        explored.add(node)

        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in explored:
                new_g = g + step_cost
                new_f = new_g + h.get(neighbor, float('inf'))
                heapq.heappush(frontier, (new_f, neighbor, path + [neighbor], new_g))

    return None, float("inf")

# Graph (same as UCS)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'E': 5},
    'C': {'E': 8},
    'D': {'G': 1},
    'E': {'G': 2},
    'G': {}
}

h = {
    'A': 10,
    'B': 6,
    'C': 7,
    'D': 3,
    'E': 2,
    'G': 0
    }

path, cost = a_star_search(graph, 'A', 'G', h)
print("Path:", path)
print("Total Cost:", cost)
