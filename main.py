import bfs, dfs, astar

URL = 'grid.txt'

def load_grid(url):
    grid = None
    with open(url, "r") as file:
        grid = file.read().split("\n")
    for i, line in enumerate(grid):
        grid[i] = list(line)
    return grid

def main():
    grid = load_grid(URL)
    start = (1,0)
    end = (18,9)

    bfs_len, bfs_grid = bfs.bfs(grid, start, end)
    dfs_len, dfs_grid = dfs.dfs(grid, start, end)
    astar_len, astar_grid = astar.astar(grid, start, end)

    print(f"BFS-grid (len = {bfs_len}):\n{bfs_grid}")
    print(f"DFS-grid (len = {dfs_len}):\n{dfs_grid}")
    print(f"A*-grid (len = {astar_len}):\n{astar_grid}")

if __name__ == '__main__':
    main()