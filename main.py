graph = {
    "A": ["B"],
    "B": []
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

def count_sink_nodes(graph):
    count = 0

    for node in graph:
        if not graph[node]:
            count += 1

    return count


print("DFS Traversal:")
dfs(graph, "A")

print("\nSink Nodes:")
for node in graph:
    if not graph[node]:
        print(node)

print("Number of Sink Nodes:", count_sink_nodes(graph))
