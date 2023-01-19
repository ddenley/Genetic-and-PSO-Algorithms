from GA import GA
import numpy as np
from matplotlib import pyplot as plt

# This code is deprecated as the graphs provided little info
def plot_graph():
    x = []
    y = []
    for generation in range(len(genetic_algo.generation_func_outputs)):
        x.append(generation)
        y.append(genetic_algo.generation_func_outputs[generation])
    plt.title("Finding Lowest Function Output - Genetic Algorithm")
    plt.xlabel("Generation")
    plt.ylabel("Function Output")
    #plt.ylim(top=0.3)
    plt.plot(x, y)
    plt.show()

iterations = 10
problem = 3
algo_generations = 2000

genetic_algo = GA(problem, 10, 30, algo_generations, 8, 0.675, 0.45, False)
func_outputs = []
for iteration in range(iterations):
    print(iteration + 1)
    genetic_algo.perform_genetic_algorithm()
    print(genetic_algo.final_outputs[1])
    func_outputs.append(genetic_algo.final_outputs[1])
    #plot_graph()

print("***Mean function output***")
print(np.mean(func_outputs))


