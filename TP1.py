# REQUIREMENT 1: Implement Path-Existance and test checking for the graph 
#   in Preference Program Language where obey following behaviors:
#       1. Ask user input 2 nodes.
#       2. Return True if path exist. Else, False.

# Student: TẠ MINH HIẾU     Student ID: 22BI13161

from collections import deque

def path_exists(graph, start, end):
    if start not in graph or end not in graph:
        print(f"Error: Node {start if start not in graph else end} does not exist in the graph.")
        return False

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return False

if __name__ == "__main__":
    graph = {
        "1": ["2"],
        "2": ["1", "5"],
        "3": ["6"],
        "4": ["6", "7"],
        "5": ["3"],
        "6": ["3", "4", "7"],
        "7": ["4", "6"]
    }

    # User input nodes
    start_node = int(input("Enter the start node: "))
    end_node = int(input("Enter the end node: "))

    # Check if path exists
    if path_exists(graph, start_node, end_node):
        print(f"Path exists between {start_node} and {end_node}")
    else:
        print(f"No path exists between {start_node} and {end_node}")
