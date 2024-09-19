"""A star"""
from bfs import grid_get


def reconstruct(grid, root, node):
    path = set()
    while node is not None:
        path.add(node)
        node = root.get(node)

    grid_route = ""
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if (x, y) in path:
                grid_route += '*'
            else:
                grid_route += grid[y][x]
        grid_route += '\n'

    return len(path), grid_route


def h(cords, end):
    """Manhattan distance"""
    return abs(cords[0]-end[0])+abs(cords[1]-end[1])


def astar(grid, start, end):
    """A-star search algorithm"""
    g_scores = {}
    f_scores = {}
    root = {}
    nodes = {start}
    g_scores[start] = 0
    f_scores[start] = h(start, end)
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while len(nodes) > 0:
        current = min(nodes, key=lambda x: f_scores.get(x))
        nodes.remove(current)
        if current == end:
            return reconstruct(grid, root, end)
        current_g_score = g_scores.get(current)
        for d in dirs:
            temp = (d[0]+current[0], d[1]+current[1])
            if grid_get(grid, temp) == '1':
                if g_scores.get(temp) is None or g_scores.get(temp) > current_g_score+1:
                    g_scores[temp] = current_g_score+1
                    f_scores[temp] = current_g_score+1+h(temp, end)
                    root[temp] = current
                    if temp not in nodes:
                        nodes.add(temp)
    return reconstruct(grid, None, None)
