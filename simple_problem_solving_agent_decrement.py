# problem solving agent 

seq = []
state = None
goal = None
problem = None

def update_state(state, percept):
    return percept
def formulate_goal(state):
    return 0
def formulate_problem(state, goal):
    return (state, goal)

def search(problem):
    state, goal = problem
    if state < goal:
        return []
    return ["Decrement "] * (state - goal)

def simple_problem_solving(percept):
    global state, goal, seq, problem
    
    state = update_state(state, percept)
    if not seq:
        goal = formulate_goal(state)
        problem = formulate_problem(state, goal)
        seq = search(problem)
        if not seq:
            return None
    
    action = seq[0]
    seq = seq[1:]
    return action

for p in [5,4,3,2,1]:
    print("Percept", p, "-> Action is", simple_problem_solving(p))