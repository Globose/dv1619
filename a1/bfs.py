"""BFS module"""
from collections import deque


def grid_get(grid, cords):
    """Returns a square from the grid, if there is one"""
    if cords[0] >= len(grid[0]) or cords[0] < 0:
        return None
    if cords[1] >= len(grid) or cords[1] < 0:
        return None
    return grid[cords[1]][cords[0]]


def reset_grid(grid, path):
    """Resets grid and returns path"""
    grid_route = ""
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square != '1' and square != '0':
                if (x, y) in path:
                    grid_route += '*'
                else:
                    grid_route += '1'
                grid[y][x] = '1'
            else:
                grid_route += square
        grid_route += '\n'
    return grid_route


def track_grid(grid, end):
    """Starts from end and tracks grid back to the start"""
    path = {end}
    next_square = grid_get(grid, end)
    while next_square is not None:
        path.add(next_square)
        next_square = grid_get(grid, next_square)
    return path


def bfs(grid, start, end):
    """Breadth-first-search"""
    queue = deque()  # Queue to store next squares to visit
    queue.append(start)
    grid[start[1]][start[0]] = None
    dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

    while len(queue) > 0:
        current = queue.popleft()  # Remove next square from queue
        if current == end:
            break
        for d in dirs:
            temp = (d[0]+current[0], d[1]+current[1])
            square = grid_get(grid, temp)
            if square == '1':
                queue.append(temp)
                grid[temp[1]][temp[0]] = current  # Store parent square

    path = {}
    if grid_get(grid, end) != '1':
        path = track_grid(grid, end)
    bfs_grid = reset_grid(grid, path)
    return len(path), bfs_grid
