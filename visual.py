import math
import tkinter as tk
import random

def draw_graph(graph, width=800, height=600, radius=20, margin=10):
    # Window root and canvas setup
    root = tk.Tk()
    canvas = tk.Canvas(root, bg='white', width=width, height=height)

    # Get vertex count from the graph
    n = graph.vertices_count()

    # Compute grid size to place each vertex evenly
    rows = cols = math.ceil(math.sqrt(n))

    cell_width = width / cols
    cell_height = height / rows

    # Key = vertex num : value = canvas circle info
    circle_data = {}

    # Place each vertex on the canvas
    for i in range(n):
        # Determine row/column index in grid
        row = i // cols
        col = i % cols

        # Top-left corner of the current cell
        x_start = col * cell_width
        y_start = row * cell_height

        # Random circle placement within assigned cell, avoiding edges
        x = random.randint(int(x_start + margin), int(x_start + cell_width - 2 * radius - margin))
        y = random.randint(int(y_start + margin), int(y_start + cell_height - 2 * radius - margin))

        # Letter label for the vertex (e.g., 'a', 'b', ...)
        label = chr(97 + i)

        # Center coordinates of each vertex circle
        center_x = x + radius
        center_y = y + radius

        # Draw the vertex as a circle
        circle_id = canvas.create_oval(
            x, y, x + 2 * radius, y + 2 * radius,
            outline='black', width=2, fill='white'
        )

        # Draw the label inside the circle
        canvas.create_text(center_x, center_y, text=label, font=("Arial", 14), fill='black')

        # Store canvas and positional data for the vertex
        circle_data[i] = {
            'id': circle_id,
            'label': label,
            'x': center_x,
            'y': center_y
        }

    # Draw edges between vertices
    def connect():
        for edge in graph.get_unique_edges():
            v_1 = edge[0]
            v_2 = edge[1]

            if v_1 != v_2:  # Regular edge (not self-loop)
                c_1 = circle_data[v_1]
                c_2 = circle_data[v_2]

                x1, y1 = c_1['x'], c_1['y']
                x2, y2 = c_2['x'], c_2['y']

                # Vector from vertex 1 to vertex 2
                dx = x2 - x1
                dy = y2 - y1
                distance = math.hypot(dx, dy)

                # Offset endpoints to avoid drawing through the circles
                x1_adj = x1 + radius * dx / distance
                y1_adj = y1 + radius * dy / distance
                x2_adj = x2 - radius * dx / distance
                y2_adj = y2 - radius * dy / distance

                # Draw edge line between adjusted points
                canvas.create_line(x1_adj, y1_adj, x2_adj, y2_adj, fill='black', width=2)

            else:  # Self-loop: draw a slightly larger circle around the vertex
                c = circle_data[v_1]
                cx, cy = c['x'], c['y']
                loop_offset = 10  # Loop distance from circle

                canvas.create_oval(
                    cx - radius - loop_offset,
                    cy - radius - loop_offset,
                    cx + radius + loop_offset,
                    cy + radius + loop_offset,
                    outline='black',
                    width=2,
                    dash=(3, 2)  # Optional dashed styling
                )

    # Draw all connections
    connect()
    canvas.pack()
    root.mainloop()