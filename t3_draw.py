import turtle as t

def draw_line(x, y, length, dir):
    xo = -350
    yo = 270
    bsize = 35
    t.up()
    t.goto(x*bsize+xo, y*bsize+yo)
    t.down()
    t.setheading(dir)
    t.forward(bsize*length)

def draw_maze(width, height, vlines, hlines, anim = False):
    t.speed(1)
    if not anim:
        t.Screen().tracer(0)
    
    t.color("blue")
    draw_line(0,0,2**0.5,315)
    draw_line(0,-1,2**0.5,45)

    t.color("red")
    draw_line(18,-6,2**0.5,315)
    draw_line(18,-7,2**0.5,45)
    
    t.color("black")
    draw_line(0, 0, width, 360)
    draw_line(0, -height, height, 90)
    
    for i, lines in enumerate(vlines):
        x = 0
        for line in lines:
            x += line
            draw_line(x, -i, 1, 270)

    for i, lines in enumerate(hlines):
        y = 0
        for line in lines:
            y += line
            draw_line(i, -y, 1, 0)

    if not anim:
        t.Screen().update()
    t.done()

def draw_solution():
    t.color("green")