import numpy as np
from random import randrange, choice

def create_population(population_size, genome_length):
    population = []
    for _ in range(population_size):
        genome = np.random.randint(0, 4, genome_length, dtype=np.uint8)
        population.append(genome)
    return population

def fitness(genome, walls, start, end):
    path_len = 0
    x,y = start
    visited = set()

    while path_len < len(genome):
        dir = genome[path_len]
        fail = False
        if dir == 0: # right
            fail = walls[y][x+1] % 3 == 0
            if not fail:
                x += 1 
        elif dir == 1: # down
            fail = walls[y+1][x] % 2 == 0
            if not fail:
                y += 1
        elif dir == 2: # left
            fail = walls[y][x] % 3 == 0
            if not fail:
                x -= 1
        else: # up
            fail = walls[y][x] % 2 == 0
            if not fail:
                y -= 1
        
        if (x,y) in visited:
            fail = True
        else:
            visited.add((x,y))
        path_len += 1
        if fail:
            path_len -= 1
            break
    return path_len

def eval_population(population, walls, start, end):
    fitness_values = []
    for genome in population:
        fitness_values.append(fitness(genome, walls, start, end))
    return np.array(fitness_values)

def select_parents(population, fitness_values):
    probabilities = fitness_values/fitness_values.sum()
    indices = np.arange(len(population))
    parents = np.random.choice(indices, size=len(population), p=probabilities)
    parents_list = [population[i] for i in parents]
    return parents_list

def crossover(parent1, parent2, crossover_rate):
    if np.random.rand() < crossover_rate:
        child1 = np.array([choice([a,b]) for a,b in zip(parent1, parent2)])
        child2 = np.array([choice([a,b]) for a,b in zip(parent1, parent2)])
        return child1, child2
    else:
        return parent1, parent2

def mutate(genome, mutation_rate):
    for i, g in enumerate(genome):
        if np.random.rand() < mutation_rate:
            genome[i] = np.random.randint(0,4)
    return genome

def genetic_algorithm(population_size, generations, mutation_rate, crossover_rate, genome_length, walls, start, end):
    population = create_population(population_size, genome_length)
    for m in range(generations):
        fitness_values = eval_population(population, walls, start, end)
        parent_list = select_parents(population, fitness_values)
        
        new_population = []
        for i in range(0, population_size, 2):
            child1, child2 = crossover(population[i], population[i+1], crossover_rate)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        best = max(population, key=lambda x: fitness(x, walls, start, end))
        new_population.append(best)
        population = new_population
        if m % 1000 == 0:
            print(fitness(best, walls, start, end))

    best = max(population, key=lambda x: fitness(x, walls, start, end))
    return best
    