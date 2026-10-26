def addEdge(adj, u, v):
    adj[u].append(v)
    adj[u].append(u)


def DFSUnil(u, adj, visted):
    visted[u] = True
    for i in range(len(adj[u])):
        if (visted[adj[u][i]] == False):
            DFSUnil(adj[u][i], adj, visted)


def countTrees(adj, V):
    visted = [False] * V
    res = 0
    for u in range(V):
        if (visted[u] == False):
            DFSUnil(u, adj, visted)
            res +=1
    return res

# Driver code

if __name__ == '__main__':

    V = 5

    adj = [[] for i in range(V)]

    addEdge(adj, 0, 1)

    addEdge(adj, 0, 2)

    addEdge(adj, 0, 3)

    addEdge(adj, 3, 4)

    print(countTrees(adj, V))