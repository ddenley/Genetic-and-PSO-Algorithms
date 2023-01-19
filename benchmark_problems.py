import optproblems
from optproblems import cec2005 as problems

class Problem:

    def __init__(self, problem, dim):
        self.dim = dim
        if problem == 1:
            self.cec2005_problem = problems.F1(dim)
            self.low_bound = -100
            self.high_bound = 100
        elif problem == 2:
            self.cec2005_problem = problems.F4(dim)
            self.low_bound = -100
            self.high_bound = 100
        elif problem == 3:
            self.cec2005_problem = problems.F9(dim)
            self.low_bound = -5
            self.high_bound = 5
        elif problem == 4:
            self.cec2005_problem = problems.F8(dim)
            self.low_bound = -100
            self.high_bound = 100
        elif problem == 5:
            self.cec2005_problem = problems.F18(dim)
            self.low_bound = -5
            self.high_bound = 5

    def evaluate_individual_solution(self, solution):
        individual = optproblems.Individual(phenome=solution)
        self.cec2005_problem.evaluate(individual)
        return individual.objective_values

    def individual_fitness(self, solution):
        return 1 / self.evaluate_individual_solution(solution)


# problem = Problem(problem=1, dim=10)
# test_solution_np = np.random.uniform(low=-100, high=100, size=10)
# print(problem.evaluate_individual_solution(test_solution_np))
# print(problem.individual_fitness(test_solution_np))



