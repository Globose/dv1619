import numpy as np

def create_population(population_size, genome_length):
    population = []
    for _ in range(population_size):
        genome = np.random.randint(0, 4, genome_length, dtype=np.uint8)
        population.append(genome)
    print(population)
    return population

def fitness(genome):
    return 0

def eval_population(population):
    fitness_values = []
    for genome in population:
        fitness_values.append(fitness(genome))
    return np.array(fitness_values)

def select_parents(population, fitness_values):
    pass