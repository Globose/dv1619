import numpy as np
from random import randrange, choice

dir = ((1,0), (0,1), (-1,0), (0,-1))
block = ((1,0,3), (0,1,2), (0,0,3), (0,0,2))

def create_population(population_size, genome_length):
    """Creates a randomly generated population of given size and length"""
    population = []
    for _ in range(population_size):
        genome = np.random.randint(0, 4, genome_length, dtype=np.uint8)
        population.append(genome)
    return population

def distance(x,y,x2,y2):
    """Calculates distance between two points"""
    return ((x-x2)**2+(y-y2)**2)**0.5

def fitness_result(dist_goal, wall_bumps_prtg, finished, explored):
    """Calculates fitness score"""
    score = dist_goal*2
    score *= (1-wall_bumps_prtg)
    score += explored
    if finished:
        score *= 1.5
    if score < 0:
        score = 1
    return score

def fitness(genome, walls, start, end):
    """Fitness function for genetic algorithm"""
    path_len = 0
    x,y = start
    visited = {(x,y)}
    step = 0
    wall_bumps = 0
    finished = False

    # Step through maze based on genome
    while step < len(genome):
        d = genome[step]
        new_node = (x+dir[d][0], y+dir[d][1])

        # Collision detection
        fail = walls[y+block[d][1]][x+block[d][0]] % block[d][2] == 0

        # If true, visit new node
        if new_node not in visited and not fail:
            visited.add(new_node)
            x = new_node[0]
            y = new_node[1]
            path_len += 1
            if x == end[0] and y == end[1]:
                finished = True
                break
        else:
            wall_bumps += 1
        step += 1
    
    # Calculate distance to goal node
    dist_goal = distance(start[0],start[1],end[0],end[1])-distance(x,y,end[0],end[1])
    return fitness_result(dist_goal, wall_bumps/len(genome), finished, len(visited))

def eval_population(population, walls, start, end):
    """Evaluate population fitness"""
    fitness_values = []
    for genome in population:
        fitness_values.append(fitness(genome, walls, start, end))
    return np.array(fitness_values)

def select_parents(population, fitness_values):
    """Returns parents based on fitness"""
    probabilities = fitness_values/fitness_values.sum()
    indices = np.arange(len(population))
    parents = np.random.choice(indices, size=len(population), p=probabilities)
    parents_list = [population[i] for i in parents]
    return parents_list

def crossover(parent1, parent2):
    """Returns 2 children based on two parents"""
    co_count = (int)(np.random.rand()*(len(parent1)+1))
    child1 = np.array(np.concatenate([parent1[:co_count],parent2[co_count:]]))
    child2 = np.array(np.concatenate([parent2[:co_count],parent1[co_count:]]))
    return child1, child2

def mutate(genome, mutation_rate):
    """Mutates a child genome randomly"""
    if np.random.rand() < mutation_rate:
        genome[np.random.randint(0,len(genome))] = np.random.randint(0,4)
    return genome

def genetic_algorithm(population_size, generations, mutation_rate, genome_length, walls, start, end):
    """Genetic algorithm main function"""
    population = create_population(population_size, genome_length)

    # Loop for generations
    for m in range(generations):
        fitness_values = eval_population(population, walls, start, end)
        population = select_parents(population, fitness_values)
        
        new_population = []
        for i in range(0, population_size, 2):
            child1, child2 = crossover(population[i], population[i+1])
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))

        population = new_population
        if m % 100 == 0:
            # Print best current score
            best = max(population, key=lambda x: fitness(x, walls, start, end))
            print(fitness(best, walls, start, end))

    return best
    