import heapq
def uniform_cost_search(graph, start, goal):
    frontier = [(0, start, [start])]
    explored = set()
    
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return cost, path
        
        if node in explored:
            continue
        
        explored.add(node)
        
        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + step_cost, neighbor, path + [neighbor]))
    return None, float('inf')


graph = {
    'A' : {'B':1,'C':4},
    'B' : {'A':1,'D':2, 'E':5},
    'C' : {'A':4,'F':3},
    'D' : {'B':2},
    'E' : {'B':5,'F':1},
    'F' : {'C':3,'E':1}
}
cost , path = uniform_cost_search(graph, 'A', 'F')
print("Path: ", path)
print("Total cost: ", cost)