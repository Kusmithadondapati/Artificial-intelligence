import random

knapsack_capacity = 50
item_weights = [15, 25, 35, 45, 65]
item_values = [60, 90, 120, 140, 210]
population_size = 50
generations = 100
mutation_rate = 0.1

def generate_chromosome():
    return [random.choice([0, 1]) for _ in range(len(item_weights))]

def initialize_population():
    return [generate_chromosome() for _ in range(population_size)]

def calculate_fitness(chromosome):
    total_value = sum(v * c for v, c in zip(chromosome, item_values))
    total_weight = sum(w * c for w, c in zip(chromosome, item_weights))
    return total_value if total_weight <= knapsack_capacity else 0

def select_parents(population):
    fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_scores)
    parents = []

    while len(parents) < population_size:
        selected_index = random.choices(range(len(population)), weights=fitness_scores)[0]
        parents.append(population[selected_index])
    
    return parents

def crossover(parent1, parent2):
    if random.random() < 0.9:
        point = random.randint(1, len(parent1) - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    return parent1, parent2

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

def genetic_algorithm():
    population = initialize_population()
    for _ in range(generations):
        population = select_parents(population)
        offspring = []
        for i in range(0, len(population) - 1, 2):
            child1, child2 = crossover(population[i], population[i + 1])
            mutate(child1)
            mutate(child2)
            offspring.extend([child1, child2])
        population = offspring

    best_solution = max(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

best_solution, best_fitness = genetic_algorithm()
print("Best Solution (Selected items):", best_solution)
print("Best Fitness (Total value):", best_fitness)
