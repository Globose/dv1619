from t3_draw import draw, draw_solution, draw_genome
import t3_ga as ga
import t3_load as maze_data
import numpy as np

def main():
    """Main function"""
    start = maze_data.get_start()
    end = maze_data.get_end()
    walls = maze_data.get_walls()
    draw(walls, anim=False)

    genome = ga.genetic_algorithm(100, 10000, .1, .5, 20, walls, start, end)
    length = ga.fitness(genome, walls, start, end)
    draw_genome(genome, start, length)

if __name__ == '__main__':
    main()