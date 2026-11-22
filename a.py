nodes = [2, 8, 5, 3]
lowest = min(nodes)

new = int(input("Enter a new number: "))

nodes.append(new)

if new < lowest:
    lowest = new

print(lowest)