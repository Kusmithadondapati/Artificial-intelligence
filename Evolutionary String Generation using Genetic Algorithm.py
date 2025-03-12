import random

POPULATION_SIZE = 100

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '''

TARGET = "ajay"

class Individual:

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def mutated_gene(cls):
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        return [cls.mutated_gene() for _ in range(len(TARGET))]

    def mate(self, partner):
        child_chromosome = []

        for gene1, gene2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(gene1)
            elif prob < 0.90:
                child_chromosome.append(gene2)
            else:
                child_chromosome.append(self.mutated_gene())

        return Individual(child_chromosome)

    def calculate_fitness(self):
        return sum(1 for gene, target_gene in zip(self.chromosome, TARGET) if gene != target_gene)

def initialize_population():
    return [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

def select_parents(population):
    return random.sample(population, 2)

def crossover(parent1, parent2):
    child_chromosome = [
        gene1 if random.random() < 0.45 else gene2 if random.random() < 0.90 else Individual.mutated_gene()
        for gene1, gene2 in zip(parent1.chromosome, parent2.chromosome)
    ]
    return Individual(child_chromosome)

def mutate_chromosome(chromosome):
    return [random.choice(GENES) if random.random() < 0.1 else gene for gene in chromosome]


def mutate(individual):
    return Individual(mutate_chromosome(individual.chromosome))

def main():
    global POPULATION_SIZE
    generation = 0
    population = initialize_population()

    while True:
        population = sorted(population, key=lambda x: x.fitness)

        best_individual = population[0]
        best_string = "".join(best_individual.chromosome)

        print(f"Generation {generation}: Best candidate = \"{best_string}\" | Fitness = {best_individual.fitness}")

        if best_individual.fitness == 0:
            print(f"Target found in generation {generation}: {best_string}")
            break

        new_generation = population[:int(0.1 * POPULATION_SIZE)]

        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            new_generation.append(child)

        population = new_generation
        generation += 1


if __name__ == "__main__":
    main()
