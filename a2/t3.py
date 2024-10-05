from t3_draw import draw, draw_genome
import t3_ga as ga
import t3_load as maze_data
import numpy as np

def main():
    """Main function"""
    start = maze_data.get_start()
    end = maze_data.get_end()
    walls = maze_data.get_walls()
    draw(walls, start, end, anim=False)
    genome = ga.genetic_algorithm(60, 1000, 0.9, 60, walls, start, end)
    draw_genome(genome, walls, start, end)

if __name__ == '__main__':
    main()