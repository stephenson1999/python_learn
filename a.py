
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}


def dfs(current, destination, path):
    path = path + [current]

 
    if current == destination:
        print("Path found:", path)
        return 1

    total = 0


    for neighbor in graph[current]:
        if neighbor not in path:
            total += dfs(neighbor, destination, path)

    return total


start = "A"
end = "D"

answer = dfs(start, end, [])

print("Total number of paths:", answer)
