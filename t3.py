from t3_draw import draw_maze
import t3_ga as ga

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

def main():
    """Main function"""
    width = get_maze_data("width")[0][0]
    height = get_maze_data("height")[0][0]
    vlines = get_maze_data("vlines")
    hlines = get_maze_data("hlines")
    # ga.create_population(10, width*height)
    draw_maze(width, height, vlines, hlines, anim=True)

if __name__ == '__main__':
    main()