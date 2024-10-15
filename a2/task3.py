from task3_draw import draw, draw_genome
import task3_ga as ga
import task3_load as maze_data
import numpy as np

def main():
    """Main function"""
    # Load maze info
    start = maze_data.get_start()
    end = maze_data.get_end()
    walls = maze_data.get_walls()

    # Draw maze
    draw(walls, start, end, anim=False)

    # Genetic algorithm
    genome = ga.genetic_algorithm(60, 600, 0.2, 60, walls, start, end)
    
    # Draw best genome path
    draw_genome(genome, walls, start, end)

if __name__ == '__main__':
    main()