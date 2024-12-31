from abc import ABC, abstractmethod
import numpy as np

class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population, fitness_scores):
        raise NotImplementedError

# 1번 : 선택 전략
class TournamentSelection(SelectionStrategy):
    # 최적 점수, 500개의 population, tournament_size=10
    def select(self, fitness_scores, num_parents, tournament_size=10):
        parents_indices = []
        for _ in range(num_parents):
            # randomly select tournament_size individuals
            tournament_indices = np.random.choice(np.arange(len(fitness_scores)), size=tournament_size, replace=False)
            tournament_fitness_scores = [fitness_scores[i] for i in tournament_indices]
            winner_index = np.argmin(tournament_fitness_scores)
            tournament_winner = tournament_indices[winner_index]
            parents_indices.append(tournament_winner)

        return np.array(parents_indices)

class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1, parent2, crossover_probability=0.99):
        raise NotImplementedError

# 2번
class OrderedCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2, crossover_probability=0.99):
        size = len(parent1)  # assuming parent1 and parent2 are of the same size
        start, stop = sorted(np.random.choice(range(size), 2, replace=False))
        child = [None] * size
        child[start:stop] = parent1[start:stop]
        remaining_elements = [element for element in parent2 if element not in parent1[start:stop]]
        current_index = 0
        for i in range(size):
            if child[i] is None:
                child[i] = remaining_elements[current_index]
                current_index += 1
        return child


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, individual, mutation_rate):
        raise NotImplementedError

# 3번
class InversionMutation(MutationStrategy):
    def mutate(self, individual, mutation_rate=None):
        individual = individual.copy()
        if np.random.rand() < mutation_rate:
            start, stop = sorted(np.random.choice(range(len(individual)), 2, replace=False))
            individual[start:stop] = individual[start:stop][::-1]
        return individual