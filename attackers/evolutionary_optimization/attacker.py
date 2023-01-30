from attackers.evolutionary_optimization.evopt import OptimizerFactory


class AttackEvo:
    def __init__(self, attack_algorithm: str = "dea"):
        self.attack_algorithm = attack_algorithm

        OPTIONS = ['ga', 'pso', 'dea', 'nm', 'bfgs', 'pow', 'bh']
        assert self.attack_algorithm in OPTIONS

    def configurate(self):
        # initiate a black-box optimizer
        PARAM_COUNT = 5

        optimizer_obj = OptimizerFactory.create(option=self.attack_algorithm, param_count=PARAM_COUNT)

        # set hyper-parameters, optional
        optimizer_obj.optimizer.population_size = 20
        optimizer_obj.optimizer.max_iterations = 50000

        return optimizer_obj

    def attack(self, objective_function):
        optimizer = self.configurate()
        # optimize, print progress to standard out, and return solution
        best_params = optimizer.maximize(objective_function)

        # evaluate final solution to obtain the optima fitness
        best_fitness = objective_function(best_params)
        return best_params, best_fitness
