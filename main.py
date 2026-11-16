v = 4
INF = 99999
def flyod(graph):
    dist = [row[:]for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    printSolution(dist)

def printSolution(dist):
    print("Matrix that shows for every vertice the shortest distance")
    for i in range(v):
        for j in range(v):
            if dist[i][j]==INF:
                print("INF",end=" ")
            else:
                print("%7d"%dist[i][j],end=" ")
        print(" ")
if __name__=="__main__":
    graph=[[0,5,INF,10],
           [INF,0,3,INF],
           [INF,INF,0,1],
           [INF,INF,INF,0]]
    flyod(graph)

