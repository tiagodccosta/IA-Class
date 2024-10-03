import matplotlib.pyplot as plt
from queue import PriorityQueue

# Adjacency list representation of the maze
# Adjacency list representation of the corrected maze

# Updated adjacency list representation of the corrected maze
maze = {
    'A': ['B', 'F'],             # North and east
    'B': ['A'],        # West, east, and south
    'C': ['D', 'H'],             # West and east
    'D': ['C', 'E'],        # West, east, and south
    'E': ['D', 'J'],             # West and south

    'F': ['A', 'G'],        # North, east, and south
    'G': ['F', 'H'],             # West and east
    'H': ['C', 'G', 'I'],        # West, east, and south
    'I': ['H', 'N'],        # West, north, and east
    'J': ['E'],                  # Only path is north

    'K': ['P'],        # North, east, and south
    'L': ['M', 'Q'],             # West and east
    'M': ['L', 'N', 'R'],             # West and east
    'N': ['M', 'O', 'I'],        # West, east, and south
    'O': ['N'],             # West and south

    'P': ['K', 'U'],             # North and east
    'Q': ['L', 'V'],             # West and east
    'R': ['M', 'S'],             # West and east
    'S': ['R', 'T'],        # North, west, and east
    'T': ['S', 'Z'],             # North and west

    'U': ['P', 'V'],             # North and east
    'V': ['U', 'X', 'Q'],             # West and east
    'X': ['V', 'Y'],             # West and east
    'Y': ['X', 'Z'],              # West and east
    'Z': ['Y', 'T'],                   # Only path is west
}

# Cells in the maze
cells = [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'X', 'Y', 'Z'
    ]

cell_positions = {
        'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
        'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 4),
        'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
        'P': (3, 0), 'Q': (3, 1), 'R': (3, 2), 'S': (3, 3), 'T': (3, 4),
        'U': (4, 0), 'V': (4, 1), 'X': (4, 2), 'Y': (4, 3), 'Z': (4, 4)
    }

# Assuming the `maze_corrected` adjacency list has been defined as above
def draw_maze(maze, cells, cell_positions):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw grid lines
    for x in range(6):
        ax.plot([x, x], [0, 5], color='black', linewidth=1)
    for y in range(6):
        ax.plot([0, 5], [y, y], color='black', linewidth=1)

    

    # Draw walls based on missing connections
    for cell, position in cell_positions.items():
        x, y = position
        
        # Check if there's a connection in the maze structure
        if cell in maze:
            neighbors = maze[cell]

            # North wall
            if (x > 0 and cells[(x - 1) * 5 + y] not in neighbors) or x == 0:
                ax.plot([y, y + 1], [x, x], color='black', linewidth=4)

            # South wall
            if (x < 4 and cells[(x + 1) * 5 + y] not in neighbors) or x == 4:
                ax.plot([y, y + 1], [x + 1, x + 1], color='black', linewidth=4)

            # West wall
            if (y > 0 and cells[x * 5 + (y - 1)] not in neighbors) or y == 0:
                ax.plot([y, y], [x, x + 1], color='black', linewidth=4)

            # East wall
            if (y < 4 and cells[x * 5 + (y + 1)] not in neighbors) or y == 4:
                ax.plot([y + 1, y + 1], [x, x + 1], color='black', linewidth=4)
    
    # Set the labels for the cells
    start_label = "Start"
    goal_label = "Goal"

    # Filling in labels
    x_offset = 0.5
    y_offset = 0.5
    for cell, (row, col) in cell_positions.items():
        if cell == 'U':
            ax.text(col + x_offset, row + y_offset, f'{cell}\n{start_label}', ha='center', va='center', fontsize=12, color="blue")
        elif cell == 'E':
            ax.text(col + x_offset, row + y_offset, f'{cell}\n{goal_label}', ha='center', va='center', fontsize=12, color="green")
        else:
            ax.text(col + x_offset, row + y_offset, cell, ha='center', va='center', fontsize=12)

    # Set plot limits, turn off axis
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    plt.gca().invert_yaxis()
    ax.axis('off')

    plt.show()



# draw maze
draw_maze(maze, cells, cell_positions)

def heuristic(cell, goal):
    x1, y1 = cell_positions[cell]
    x2, y2 = cell_positions[goal]
    return abs(x1 - x2) + abs(y1 - y2)

def A_Star_Path(maze, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))

    g_cost = {start: 0}

    while not pq.empty():
        _, current_cell, path = pq.get()

        if current_cell == goal:
            return path

        for neighbor in maze[current_cell]:
            g = g_cost[current_cell] + 1

            if neighbor not in g_cost or g < g_cost[neighbor]:
                g_cost[neighbor] = g
                f = g + heuristic(neighbor, goal)
                pq.put((f, neighbor, path + [neighbor]))

    return None

def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_cell, path = stack.pop()
        if current_cell == goal:
            return path

        if current_cell in visited:
            continue

        visited.add(current_cell)
        for neighbor in maze[current_cell]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    
start = 'U'
goal = 'E'
print(f"DFS path from {start} to {goal}: {dfs(maze, start, goal)}")
print(f"A* path from {start} to {goal}: {A_Star_Path(maze, start, goal)}")
