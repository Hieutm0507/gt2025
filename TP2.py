# REQUIREMENT 2 (28/12/2024): 
#   * Given the directed graph as a matrix represent
#   * Return number of weakly connected component and strongly connected component

# Student: TẠ MINH HIẾU     Student ID: 22BI13161


def depthFirstSearch(graph, node, visited, stack=None):
    visited[node] = True
    for neighbor, is_connected in enumerate(graph[node]):
        if is_connected and not visited[neighbor]:
            depthFirstSearch(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(node)

def reverse_graph(graph):
    n = len(graph)
    reversed_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                reversed_graph[j][i] = 1
    return reversed_graph

# Find Strongly Connected Components
def find_scc(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            depthFirstSearch(graph, i, visited, stack)

    reversed_graph = reverse_graph(graph)

    visited = [False] * n
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            depthFirstSearch(reversed_graph, node, visited)
            scc_count += 1

    return scc_count

# Find Weakly Connected Components
def find_wcc(graph):
    n = len(graph)
    undirected_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                undirected_graph[i][j] = undirected_graph[j][i] = 1

    visited = [False] * n
    weak_components = 0
    for i in range(n):
        if not visited[i]:
            depthFirstSearch(undirected_graph, i, visited)
            weak_components += 1

    return weak_components

if __name__=="__main__":
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    weak_components = find_wcc(G)
    scc_count = find_scc(G)
    
    print("Number of Weakly Connected Components:", weak_components)
    print("Number of Strongly Connected Components:", scc_count)