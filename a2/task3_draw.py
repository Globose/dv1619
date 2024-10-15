import turtle as t

dir = ((1,0), (0,1), (-1,0), (0,-1))
block = ((1,0,3), (0,1,2), (0,0,3), (0,0,2))

def draw_line(x1, y1, x2, y2):
    bsize = 35
    xo = -350
    yo = 270
    t.up()
    t.goto(x1*bsize+xo, -y1*bsize+yo)
    t.down()
    t.goto(x2*bsize+xo, -y2*bsize+yo)

def draw(walls, start, end, anim=True):
    t.speed(1)
    if not anim:
        t.Screen().tracer(0)
    
    t.color("blue")
    draw_line(start[0],start[1], start[0]+1,start[1]+1)

    t.color("red")
    draw_line(end[0], end[1], end[0]+1,end[1]+1)
    
    t.color("black")
    for y, row in enumerate(walls):
        for x, cell in enumerate(row):
            if cell % 3 == 0:
                draw_line(x, y, x, y+1)
            if cell % 2 == 0:
                draw_line(x, y, x+1, y)
                
    if not anim:
        t.Screen().update()

def draw_genome(genome, walls, start, end):
    t.Screen().tracer(1)
    t.speed(2)
    t.color("orange")
    x,y = start
    visited = {(x,y)}
    step = 0
    while step < len(genome):
        d = genome[step]
        new_node = (x+dir[d][0], y+dir[d][1])
        fail = walls[y+block[d][1]][x+block[d][0]] % block[d][2] == 0
        if new_node not in visited and not fail:
            visited.add(new_node)
            draw_line(x+.5,y+.5,new_node[0]+.5,new_node[1]+.5)
            x = new_node[0]
            y = new_node[1]
            if x == end[0] and y == end[1]:
                break
        step += 1
    t.done()
