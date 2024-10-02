import turtle as t

def draw_line(x1, y1, x2, y2):
    bsize = 35
    xo = -350
    yo = 270
    t.up()
    t.goto(x1*bsize+xo, -y1*bsize+yo)
    t.down()
    t.goto(x2*bsize+xo, -y2*bsize+yo)

def draw(walls, anim = True):
    t.speed(1)
    if not anim:
        t.Screen().tracer(0)
    
    t.color("blue")
    draw_line(0,0, 1,1)

    t.color("red")
    draw_line(18, 6, 19,7)
    
    t.color("black")
    for y, row in enumerate(walls):
        for x, cell in enumerate(row):
            if cell % 3 == 0:
                draw_line(x, y, x, y+1)
            if cell % 2 == 0:
                draw_line(x, y, x+1, y)
                
    if not anim:
        t.Screen().update()

def draw_solution(solution_set):
    t.Screen().tracer(1)
    t.color("green")
    x1, y1 = solution_set[0]
    for cords in solution_set:
        x2, y2 = cords
        draw_line(x1+.5,y1+.5,x2+.5,y2+.5)
        x1, y1 = x2, y2
    t.done()

def draw_genome(genome, start, length):
    t.Screen().tracer(1)
    t.color("orange")
    x1, y1 = start
    x1 += .5
    y1 += .5
    path_len = 0
    for dir in genome:
        if dir == 0: # right
            draw_line(x1,y1,x1+1,y1)
            x1 += 1
        elif dir == 1: # down
            draw_line(x1,y1,x1,y1+1)
            y1 += 1
        elif dir == 2: # left
            draw_line(x1,y1,x1-1,y1)
            x1 -= 1
        else: # up
            draw_line(x1,y1,x1,y1-1)
            y1 -= 1
        path_len += 1
        if path_len >= length:
            break
    t.done()

