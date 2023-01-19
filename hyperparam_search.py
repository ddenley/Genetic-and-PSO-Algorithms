from PSO import PSO
from GA import GA
import numpy as np

# Code to search for optimal hyperparameters

#Declare problem and dimensions to test on here
problem = 1
problem_dimensions = 10

# Population size/swarm size and generation/iterations should remain the same
pop_size = 30
iterations = 200

#Amount of times to test
times_to_run = 10

def ga_range_search():
    tournament_lower = float(input("Input bottom range of tournament search: "))
    tournament_higher = float(input("Input higher range of tournament search: "))

    cross_lower = float(input("Input bottom range of cross rate: "))
    cross_higher = float(input("Input higher range of cross rate: "))

    mutation_lower = float(input("Input bottom range of mutation rate: "))
    mutation_higher = float(input("Input higher range of mutation rate: "))

    tournament_range = np.linspace(tournament_lower, tournament_higher, 10)
    cross_range = np.linspace(cross_lower, cross_higher, 5)
    mutation_range = np.linspace(mutation_lower, mutation_higher, 5)

    test_values = []
    for tvalue in tournament_range:
        for cvalue in cross_range:
            for mvalue in mutation_range:
                test_values.append((tvalue, cvalue, mvalue))

    best_output_mean = np.Inf
    best_params = []
    i = 1
    for test_values_combination in test_values:
        means = test_ga(times_to_run, test_values_combination)
        if means[1] < best_output_mean:
            best_params = test_values_combination
            best_fitness_mean = means[0]
            best_output_mean = means[1]
            print("Fitness: ", best_fitness_mean)
            print("Output: ", best_output_mean)
            print("Params: ", best_params)
        print("Combos checked: ", i, " out of ", len(test_values))
        i += 1

    print("***Best output found: ", best_output_mean, "***")
    print("With tournament size: ", int(best_params[0]), "cross rate: ", best_params[1], "mutation rate", best_params[2])


def test_ga(times_to_run, testing_values):
    tournament_size = int(testing_values[0])
    cross_rate = testing_values[1]
    mutation_rate = testing_values[2]

    run_vals_fitness = []
    run_vals_output = []
    for run in range(times_to_run):
        genetic_algo = GA(problem, problem_dimensions, pop_size, iterations, tournament_size, cross_rate, mutation_rate, False)
        genetic_algo.perform_genetic_algorithm()
        # print("Run: ", run + 1, "Fitness: ", genetic_algo.final_outputs[0], "Func Ouput: ", genetic_algo.final_outputs[1],
        #       "Generation: ", genetic_algo.generation + 1, "Tournament Size: ", genetic_algo.tournament_size,
        #       "Cross rate: ", genetic_algo.cross_rate, "Mutation rate: ", genetic_algo.mut_rate)
        run_vals_fitness.append(genetic_algo.final_outputs[0])
        run_vals_output.append(genetic_algo.final_outputs[1])

    return np.mean(run_vals_fitness), np.mean(run_vals_output)



ga_range_search()