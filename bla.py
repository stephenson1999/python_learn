def all_paths_maze(N, M):
    paths = []


    def backtrack(x, y, path):

        if x == N - 1 and y == M - 1:
            paths.append(path[:])
            return

        if y + 1 < M:
            path.append('R')
            backtrack(x, y + 1, path)
            path.pop()

        if x + 1 < N:
            path.append('D')  
            backtrack(x + 1, y, path)
            path.pop()

    backtrack(0, 0, [])
    return paths


if __name__ == "__main__":
    N = 4
    M = 4

    paths = all_paths_maze(N, M)

    print(f"All possible paths in a {N}x{M} maze moving only Right and Down:\n")
    for i, p in enumerate(paths, 1):
        print(f"Path {i}: {''.join(p)}")

    print(f"\nTotal paths: {len(paths)}")




    