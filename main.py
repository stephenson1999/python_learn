kind = input("add or mutiplay?: ")

x = [[8,2],
    [4,1]]

y = [[3,8],
     [9,15]]

answer = [[0,0], [0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        if kind == "add":
            answer[i][j] = x[i][j] + y[i][j]
        if kind == "mutiplay":
            answer[i][j] = x[i][j] * y[i][j]

print(answer)



















Nasa_discoverys_of_2026="https://www.nasa.gov/blogs/watch-the-skies/2026/01/16/most-notable-2026-astronomical-events-a-year-of-watching-the-skies/"