def get_maze_data(info):
    outlist = []
    A = None
    with open("maze.txt", "r") as file:
        A = file.read().split("\n")
    start_index = -1
    for i, a in enumerate(A):
        if a == info:
            start_index = i+1
            break
    if start_index == -1:
        return
    
    for i in range(start_index, len(A)):
        if A[i] == '':
            break
        tlist = A[i].split(',')
        outlist.append(list(map(int, tlist)))
    return outlist

def get_start():
    return get_maze_data("start")[0]

def get_width():
    return get_maze_data("width")[0][0]

def get_height():
    return get_maze_data("height")[0][0]

def get_end():
    return get_maze_data("end")[0]

def get_walls():
    width = get_maze_data("width")[0][0]
    height = get_maze_data("height")[0][0]
    vlines = get_maze_data("vlines")
    hlines = get_maze_data("hlines")
    walls = [[1 for _ in range(width+1)] for _ in range(height+1)]
    
    for i, row in enumerate(vlines):
        x_value = 0
        for vline in row:
            x_value += vline
            walls[i][x_value] *= 3
    
    for i, column in enumerate(hlines):
        y_value = 0
        for hline in column:
            y_value += hline
            walls[y_value][i] *= 2
    return walls