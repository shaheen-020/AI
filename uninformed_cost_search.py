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
    'A' : {'B':1, 'C':4},
    'B' : {'E':3, 'D':5},
    'C' : {'F':5},
    'D' : {'G':2},
    'E' : {'G':1},
    'F' : {'G':2},
    'G': {}
} 
cost , path = uniform_cost_search(graph, 'A', 'F')
print("Path: ", path)
print("Total cost: ", cost)