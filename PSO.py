import random
import numpy as np
import benchmark_problems

class PSOParticle:

    def __init__(self, problem):
        self.position = np.random.uniform(low=problem.low_bound, high=problem.high_bound, size=problem.dim)
        self.velocity = np.zeros_like(self.position)
        self.fittest_location = None
        self.informants = []
        self.best_informant = None

# Particle swarm optimization
class PSO:

    def __init__(self, problem, problem_dimensions, swarm_size, generations, prop_v, prop_pb, prop_ib, prop_gb,
                 jump_size, informant_count):
        self.problem = benchmark_problems.Problem(problem=problem, dim=problem_dimensions)
        self.swarm_size = swarm_size
        self.generations = generations
        self.prop_v = prop_v
        self.prop_pb = prop_pb
        self.prop_ib = prop_ib
        self.prop_gb = prop_gb
        self.jump_size = jump_size
        self.informant_count = informant_count
        self.best = None
        self.swarm = None

    def init_swarm(self):
        swarm = []
        for p in range(self.swarm_size):
            particle = PSOParticle(self.problem)
            swarm.append(particle)
        self.swarm = swarm

    def assign_informants(self, particle, swarm):
        # As per Metaheuristics course book informants should include particle itself
        particle.informants.append(particle)
        # Now randomly assign informant_count - 1 number of other particles as other informants
        informant_indexes = []
        i = 0
        while i < self.informant_count - 1:
            index = random.randint(0, len(swarm) - 1)
            if informant_indexes.count(index) == 0:
                informant_indexes.append(index)
                i += 1
        for index in informant_indexes:
            particle.informants.append(swarm[index])

    def perform_pso(self):
        self.init_swarm()
        for particle in self.swarm:
            self.assign_informants(particle, self.swarm)
        for generation in range(self.generations):
            # Update the best location found so far by any particle
            for particle in self.swarm:
                particle_fitness = self.problem.individual_fitness(particle.position)
                if self.best is None:
                    self.best = particle
                elif particle_fitness > self.problem.individual_fitness(self.best.position):
                    self.best = particle
            # Update the particles previous best location
            for particle in self.swarm:
                particle_fitness = self.problem.individual_fitness(particle.position)
                if particle.fittest_location is None:
                    particle.fittest_location = particle.position
                particles_prev_best_loc = self.problem.individual_fitness(particle.fittest_location)
                if particle_fitness > particles_prev_best_loc:
                    particle.fittest_location = particle.position
            # Set each particles' best informant
            for particle in self.swarm:
                for informant in particle.informants:
                    if particle.best_informant is None:
                        particle.best_informant = informant
                    else:
                        if self.problem.individual_fitness(informant.position) > \
                                self.problem.individual_fitness(particle.best_informant.position):
                            particle.best_informant = informant
            for particle in self.swarm:
                b = np.random.uniform(low=0, high=self.prop_pb, size=self.problem.dim)
                c = np.random.uniform(low=0, high=self.prop_ib, size=self.problem.dim)
                d = np.random.uniform(low=0, high=self.prop_gb, size=self.problem.dim)
                vel = (self.prop_v * particle.velocity) + (b * (particle.position - particle.fittest_location)) + (c * \
                      (particle.position - particle.best_informant.position)) + (d * (particle.position - self.best.position))
                particle.velocity = vel
                #print(vel)
                particle.position = particle.position + (self.jump_size * particle.velocity)
                particle.position[particle.position > 100] = -100
                particle.position[particle.position < -100] = 100
            print(generation)
            print(self.swarm[0].position)
            print(self.problem.individual_fitness(self.best.position))
            print(self.best)



# Recommended that acceleration coeffs sum to 4
# Testing code below

#pso = PSO(1, 10, 100, 1000, 0.9, 0.6, 0.7, 0.0, 0.2, 10)
#pso.perform_pso()