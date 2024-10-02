from queue import deque
from queue import Queue

graph = {
    '1': ['2', '9', '10'],
    '2': ['3', '4'],
    '3': [],
    '4': ['5', '6', '7'],
    '5': ['8'],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
}


print("-- Breadth First Search --")
def BFS(graph, start):  ### First In First Out
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited.append(node)
        childs = graph[node]
        for n in childs:
            if n not in visited and n not in queue:
                queue.append(n)
    return visited    

print(BFS(graph, '1'))

visited = []
print("-- Depth First Search with Recursion --") 
def DFS_Recursion(graph, start):  ### Last In First Out  
    visited.append(start)
    for n in graph[start]:
        if n not in visited:
            DFS_Recursion(graph, n)
    return visited

print(DFS_Recursion(graph, '1'))

visited = []
stack = []
print("-- Depth First Search without Recursion --") 
def DFS(graph, start):  ### Last In First Out
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            childs = graph[node]
            for n in reversed(childs):
                stack.append(n)
    return visited


print(DFS(graph, '1'))

# Uniform cost, Priority Queue - variant of queue, lowest first
from queue import PriorityQueue
# Define the graph as a dictionary of dictionaries
graph = {
    "1": {"2": 3, "3": 4, "5": 2},
    "2": {"1": 3, "4": 1, "7": 5},
    "3": {"1": 4, "5": 2, "6": 3},
    "4": {"2": 1, "8": 4},
    "5": {"1": 2, "3": 2, "7": 1},
    "6": {"3": 3, "9": 5},
    "7": {"5": 1, "2": 5, "8": 2, "10": 2},
    "8": {"4": 4, "7": 2, "10": 4},
    "9": {"6": 5, "10": 3},
    "10": {"7": 2, "8": 4, "9": 3}
}

def uniform_cost_search_pq(graph, start, goal):
# Priority Queue where the priority is the cost
    pq = PriorityQueue()
    pq.put((0, start, [])) # (cost, current_node, path)
    visited = set()

    while not pq.empty():
        cost, current_node, path = pq.get()
        if current_node == goal:
            print(cost, path + [current_node])
            return cost, path
        if current_node in visited:
            print("Is in visited " ,current_node)
            continue

        visited.add(current_node)
        print("Added to visited ", current_node)
        for neighbor, new_cost in graph[current_node].items():
            if neighbor not in visited:
                pq.put((cost + new_cost, neighbor, path + [current_node]))
                print("Added to PQ ", cost + new_cost, neighbor, path + [current_node])


# Example usage with the graph defined earlier
start_node = '1'
goal_node = '7'
cost, path = uniform_cost_search_pq(graph, start_node, goal_node)
print(f"Path from {start_node} to {goal_node}: {path} with total cost: {cost}")

#### Deepening Depth-First Search (IDDFS)
def deepening_dfs_iterative(graph, start, goal):
    depth = 0

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Fixed graph with all string keys and values
graphBDS = {
    "1": ["2", "3", "5"],
    "2": ["1", "4", "7"],
    "3": ["1", "5", "6"],
    "4": ["2", "8"],
    "5": ["1", "3", "7"],
    "6": ["3", "9"],
    "7": ["5", "2", "8", "10"],
    "8": ["4", "7", "10"],
    "9": ["6", "10"],
    "10": ["7", "8", "9"]
}

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    
    forward_queue = deque([start])
    backward_queue = deque([goal])
    
    forward_parents = {start: None}
    backward_parents = {goal: None}
    
    while forward_queue and backward_queue:
        if forward_queue:
            forward_node = forward_queue.popleft()
            for neighbor in graph[forward_node]:
                if neighbor not in forward_parents:
                    forward_parents[neighbor] = forward_node
                    forward_queue.append(neighbor)
                    
                    if neighbor in backward_parents:
                        return construct_path(forward_parents, backward_parents, neighbor)

        if backward_queue:
            backward_node = backward_queue.popleft()
            for neighbor in graph[backward_node]:
                if neighbor not in backward_parents:
                    backward_parents[neighbor] = backward_node
                    backward_queue.append(neighbor)
                    
                    if neighbor in forward_parents:
                        return construct_path(forward_parents, backward_parents, neighbor)
    
    return None

def construct_path(forward_parents, backward_parents, meeting_node):
    path_forward = []
    node = meeting_node
    while node:
        path_forward.append(node)
        node = forward_parents[node]
    
    path_backward = []
    node = backward_parents[meeting_node]
    while node:
        path_backward.append(node)
        node = backward_parents[node]
    
    return path_forward[::-1] + path_backward

start_node = '1'
goal_node = '10'
path = bidirectional_search(graphBDS, start_node, goal_node)
print(f"Path from {start_node} to {goal_node} using bidirectional search: {path}")