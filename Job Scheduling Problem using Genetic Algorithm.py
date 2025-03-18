import random 
 
NUM_JOBS = 5  
NUM_MACHINES = 2  
POPULATION_SIZE = 10  
GENERATIONS = 6
CROSSOVER_RATE = 0.8  
MUTATION_RATE = 0.1  
PROCESSING_TIMES = [3, 5, 2, 4, 1]  
 

 
def create_chromosome(): 
    return [random.randint(0, NUM_MACHINES - 1) for _ in range(NUM_JOBS)] 
 
def calculate_fitness(chromosome): 
    machine_times = [0] * NUM_MACHINES 
    for job, machine in enumerate(chromosome): 
        machine_times[machine] += PROCESSING_TIMES[job] 
    return 1 / max(machine_times) 
 
def crossover(parent1, parent2): 
    if random.random() < CROSSOVER_RATE: 
        point1, point2 = sorted(random.sample(range(NUM_JOBS), 2)) 
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:] 
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:] 
        return child1, child2 
    return parent1, parent2 
def mutate(chromosome): 
    return [random.randint(0, NUM_MACHINES - 1) if random.random() < MUTATION_RATE else gene for gene in chromosome] 
 
def genetic_algorithm(): 
    population = [create_chromosome() for _ in range(POPULATION_SIZE)] 
    best_fitness = 0 
    best_chromosome = None 
 
    for generation in range(GENERATIONS): 
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population] 
        best_in_generation = max(fitness_scores) 
        if best_in_generation > best_fitness: 
            best_fitness = best_in_generation 
            best_chromosome = population[fitness_scores.index(best_in_generation)] 
 
        new_population = [] 
        while len(new_population) < POPULATION_SIZE: 
            parent1, parent2 = random.choices(population, weights=fitness_scores, k=2) 
            child1, child2 = crossover(parent1, parent2) 
            new_population.extend([mutate(child1), mutate(child2)]) 
 
        population = new_population[:POPULATION_SIZE] 
 
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}") 
 
    return best_chromosome, best_fitness 
 
best_schedule, best_fitness = genetic_algorithm() 
print("\nBest Schedule:", best_schedule) 
print("Best Fitness (1 / Completion Time):", best_fitness) 
print("Total Completion Time:", 1 / best_fitness)