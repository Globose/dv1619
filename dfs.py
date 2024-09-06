from bfs import grid_get, track_grid, reset_grid

def _dfs_r(grid, current, end, root=None):
    dirs = ((1,0),(0,1),(-1,0),(0,-1))
    grid[current[1]][current[0]] = root
    if current == end:
        return True
    for d in dirs:
        new_cord = (current[0]+d[0], current[1]+d[1])
        if grid_get(grid, new_cord) == '1':
            if _dfs_r(grid, new_cord, end, current):
                return True
    return False

def dfs(grid, start, end):
    _dfs_r(grid, start, end)
    path = {}
    if grid_get(grid,end) != '1':
        path = track_grid(grid, end)
    grid_route = reset_grid(grid, path)
    return len(path), grid_route

def main():
    grid = None
    with open('grid.txt', "r") as file:
        grid = file.read().split("\n")
        for i, line in enumerate(grid):
            grid[i] = list(line)
    path_len, dfs_grid = dfs(grid, (1,0), (18,9))
    print(dfs_grid)
    print("len:",path_len)

if __name__ == '__main__':
    main()