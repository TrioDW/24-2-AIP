from abc import ABC, abstractmethod
import numpy as np

from algorithms import OrderedCrossover
from algorithms import InversionMutation
from algorithms import TournamentSelection
from problem import Problem


class Solver(ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def solve(self):
        pass


class GeneticAlgorithmSolver(Solver):
    def __init__(
        self,
        problem: Problem,
        population_size=500,
        generations=500,
        crossover_rate=0.999,
        mutation_rate=0.01,
        selection='tournament', # torunament는 랜덤하게 선택된 부모 중 가장 좋은 부모를 선택
        crossover='ordered', # ordered는 부모의 일부를 교환
        mutation='inversion'# inversion은 일부를 뒤집음
    ):

        super().__init__(problem)
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.selection = TournamentSelection()
        self.crossover = OrderedCrossover()
        self.mutation = InversionMutation()
        
    def solve(self):
        # 500개의 랜덤 경로 생성
        population = [self.problem.initial_state() for _ in range(self.population_size)]

        # best solution 초기화
        best_solution = None
        # best score 초기화
        best_score = float('inf')

        # 500세대까지 반복
        for _ in range(self.generations):
            # 500개의 population의 적합도 평가 (총 길이)
            fitness_scores = [self.problem.objective_function(individual) for individual in population]
            
            # 적합도가 가장 좋은 것의 index 반환
            best_idx = np.argmin(fitness_scores)

            # 최적의 경로일 경우, best 값 갱신
            if (fitness_scores[best_idx] < best_score):
                best_score = fitness_scores[best_idx]
                best_solution = population[best_idx]

            # TournamentSelection을 사용해 부모 선택
            self.selection.select(fitness_scores, len(population))

        return best_solution


    def generate_new_population(self, population, selected_indexes):
        new_population = []

        for i in range(0, len(selected_indexes), 2):
            parent1, parent2 = population[selected_indexes[i]], population[selected_indexes[i+1]]

            if np.random.rand() < self.crossover_rate:
                child1 = self.crossover.crossover(parent1, parent2, self.crossover_rate)
                child2 = self.crossover.crossover(parent1, parent2, self.crossover_rate)
            else:
                child1, child2 = parent1, parent2
            child1 = self.mutation.mutate(child1, self.mutation_rate)
            child2 = self.mutation.mutate(child2, self.mutation_rate)
            new_population += [child2, child1]
        return new_population