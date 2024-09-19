"""DFS module"""
from bfs import grid_get, track_grid, reset_grid


def _dfs_r(grid, current, end, root=None):
    """Recursive dfs calculation"""
    dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))  # Right, down, left, up
    grid[current[1]][current[0]] = root
    if current == end:
        return True
    for d in dirs:  # Look in all 4 directions
        new_cord = (current[0]+d[0], current[1]+d[1])
        if grid_get(grid, new_cord) == '1':
            if _dfs_r(grid, new_cord, end, current):
                return True
    return False


def dfs(grid, start, end):
    """Depth-first-search"""
    _dfs_r(grid, start, end)  # Recursive call
    path = {}
    if grid_get(grid, end) != '1':  # True if path is found
        path = track_grid(grid, end)
    grid_route = reset_grid(grid, path)
    return len(path), grid_route
