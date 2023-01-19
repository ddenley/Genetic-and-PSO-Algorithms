import random
import numpy as np
import benchmark_problems

# Genetic Algorithm
class GA:


    def __init__(self, problem, problem_dimensions, population_size, generation_count, tournament_size, cross_rate, mut_rate, print = True):
        self.problem = benchmark_problems.Problem(problem=problem, dim=problem_dimensions)
        self.population_size = population_size
        self.generation_count = generation_count
        self.tournament_size = tournament_size
        self.cross_rate = cross_rate
        self.mut_rate = mut_rate
        self.print = print
        self.final_outputs = []
        self.generation = 0
        self.generation_func_outputs = []

    # Randomly initialize population with solution vectors of real numbers within problems range
    def init_population(self):
        population = []
        for instance in range(self.population_size):
            population.append(np.random.uniform(low=self.problem.low_bound,
                                                high=self.problem.high_bound,
                                                size=self.problem.dim))
        return population

    # By changing tournament size we specify how selective the technique is
    # As tournament size grows exploration grows, and exploitation decreases
    def tournament_selection(self, individual, population):
        best = individual
        for i in range(self.tournament_size):
            next = population[random.randint(0, self.population_size - 1)]
            best_fitness = self.problem.individual_fitness(best)
            next_fitness = self.problem.individual_fitness(next)
            if next_fitness > best_fitness:
                best = next
        return best

    # Simple mutation where we randomly change one gene/value in the vector
    def mutate(self, solution):
        index = random.randint(0, len(solution) - 1)
        solution[index] = random.uniform(a=self.problem.low_bound,
                                         b=self.problem.high_bound)
        return solution

    # Takes a random index and the values from that index to the length of the vector are switched
    def one_point_crossover(self, solution1, solution2):
        index = random.randint(0, len(solution1))
        if index != 1:
            solution1_index_vals = solution1[index:].copy()
            solution2_index_vals = solution2[index:].copy()
            solution1[index:] = solution2_index_vals
            solution2[index:] = solution1_index_vals
        return solution1, solution2


    def perform_genetic_algorithm(self):
        population = self.init_population()
        best = []
        final_outputs = [0, 0]
        for generation in range(self.generation_count):
            for individual in population:
                if len(best) == 0:
                    best = individual
                elif self.problem.individual_fitness(individual) > self.problem.individual_fitness(best):
                    best = individual
            parents = []
            for individual in population:
                # Use tournament selection to pick individuals to act as parents
                parents.append(self.tournament_selection(individual, population))
            children = []
            for i in range(int(len(population) / 2)):
                p1 = parents[i]
                p2 = parents[i+1]
                if random.random() > self.cross_rate:
                    c1, c2 = self.one_point_crossover(p1, p2)
                else:
                    c1, c2 = p1.copy(), p2.copy()
                children.append(c1)
                children.append(c2)
            children_mutated = []
            for child in children:
                if random.random() > self.mut_rate:
                    children_mutated.append(self.mutate(child))
                else:
                    children_mutated.append(child)
            population = children_mutated
            if self.print == True:
                print("Generation: ", generation + 1, " Fitness Val: ", self.problem.individual_fitness(best),
                      " Function Output: ", self.problem.evaluate_individual_solution(best))
            if generation == self.generation_count - 1:
                final_outputs[0] = self.problem.individual_fitness(best)
                final_outputs[1] = self.problem.evaluate_individual_solution(best)
                self.final_outputs = final_outputs
            self.generation = generation
            self.generation_func_outputs.append(self.problem.evaluate_individual_solution(best))



# Testing code below

#ga = GA(5, 10, 30, 10000, 8, 0.675, 0.45)
#ga.perform_genetic_algorithm()
