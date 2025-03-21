import math
import tkinter as tk
import random
from graph import Graph

# Window width and height (pixels)
WIDTH = 800
HEIGHT = 600

# Vertex count
n = 5
graph = Graph(n)

# Window root, canvas window
root = tk.Tk()
canvas = tk.Canvas(root, bg='white', width=WIDTH, height=HEIGHT)

# Rows and columns based on given node count
rows = cols = math.ceil(math.sqrt(n))

cell_width = WIDTH / cols
cell_height = HEIGHT / rows + 100

margin = 10 # Offset within each cell of each circle
radius = 20 # Circle radius

# Key = vertex num : value = canvas id
circle_data = {}

for i in range(n):
    # Determine row/column index in grid
    row = i // cols
    col = i % cols

    # Top left corner of grid cell
    x_start = col * cell_width
    y_start = row * cell_height

    # Random circle placement within assigned cell
    x = random.randint(int(x_start + margin), int(x_start + cell_width - 2 * radius - margin))
    y = random.randint(int(y_start + margin), int(y_start + cell_height - 2 * radius - margin))

    # Letter equivalent of each vertex number
    label = chr(97 + i)

    # Center coordinates of each canvas circle
    center_x = x + radius
    center_y = y + radius

    circle_id = canvas.create_oval(x, y, x + 2 * radius, y + 2 * radius, outline='black', width=2, fill='white')
    canvas.create_text(center_x, center_y, text=label, font=("Arial", 14), fill='black')


    # Map i (vertex num) to canvas circle id
    circle_data[i] = {
        'id': circle_id,
        'label': label,
        'x': center_x,
        'y': center_y
    }

def connect(): # TODO: self edge
    for edge in graph.get_unique_edges():
        # Vertex number within Graph class
        v_1 = edge[0]
        v_2 = edge[1]

        if not v_1 == v_2: # Non self-loops
            # Canvas circle data
            c_1 = circle_data[v_1]
            c_2 = circle_data[v_2]

            # Canvas circle center coordinates
            x1, y1 = c_1['x'], c_1['y']
            x2, y2 = c_2['x'], c_2['y']

            # Adjacent and opposite side of
            dx = x2 - x1
            dy = y2 - y1
            distance = math.hypot(dx, dy) # Hypotenuse right triangle

            # Move outward from center of circle 1 and inward to center of circle 2
            x1_adj = x1 + radius * dx / distance
            y1_adj = y1 + radius * dy / distance
            x2_adj = x2 - radius * dx / distance
            y2_adj = y2 - radius * dy / distance

            # Plot line of edge between given vertices
            canvas.create_line(x1_adj, y1_adj, x2_adj, y2_adj, fill='black', width=2)
        else:  # Self-loop (v_1 == v_2)
            c = circle_data[v_1]
            cx, cy = c['x'], c['y']
            loop_offset = 10  # How far the loop sits outside the original circle

            # Draw a slightly larger oval to represent the loop
            canvas.create_oval(
                cx - radius - loop_offset,
                cy - radius - loop_offset,
                cx + radius + loop_offset,
                cy + radius + loop_offset,
                outline='black',
                width=2,
                dash=(3, 2)  # Optional: dashed loop for style
            )

# Circular graph
j = 1
for i in range (n - 1):
    graph.connect([i, j])
    j += 1
graph.connect([j - 1, 0])

connect()
canvas.pack()
root.mainloop()