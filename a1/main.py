"""Main module, bfs, dfs, astar program"""
import bfs
import dfs
import astar


def main():
    """Main function"""

    # Read grid file
    grid = None
    with open("grid.txt", "r", encoding="utf-8") as file:
        grid = file.read().split("\n")
    for i, line in enumerate(grid):
        grid[i] = list(line)

    start = (1, 0)
    end = (18, 9)

    # Calculate bfs, dfs, astar
    bfs_len, bfs_grid = bfs.bfs(grid, start, end)
    dfs_len, dfs_grid = dfs.dfs(grid, start, end)
    astar_len, astar_grid = astar.astar(grid, start, end)

    # Print paths and path length
    if bfs_len > 0:
        print(f"BFS-grid (len = {bfs_len}):\n{bfs_grid}")
        print(f"DFS-grid (len = {dfs_len}):\n{dfs_grid}")
        print(f"A*-grid (len = {astar_len}):\n{astar_grid}")
    else:
        print("No path found")


if __name__ == '__main__':
    main()
