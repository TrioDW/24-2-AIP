from abc import ABC, abstractmethod
from typing import Any, List, Tuple
import numpy as np


class Problem(ABC):
    @abstractmethod
    def initial_state(self) -> Any:
        pass

    @abstractmethod
    def actions(self, state: Any) -> List[Any]:
        pass

    @abstractmethod
    def result(self, state: Any, action: Any) -> Any:
        pass

    @abstractmethod
    def goal_test(self, state: Any) -> bool:
        pass

    @abstractmethod
    def step_cost(self, state: Any, action: Any) -> float:
        pass

    @abstractmethod
    def objective_function(self, state: Any) -> float:
        pass

    @abstractmethod
    def hash_state(self, state: Any) -> int:
        pass

    @abstractmethod
    def is_valid(self, state: Any) -> bool:
        pass


class TSPProblem(Problem):
  def __init__(self, cities: np.ndarray):
    self.cities: np.ndarray = cities
    self.num_cities: int = cities.shape[0]
    self.distance_matrix: np.ndarray = self._calculate_distance_matrix()

  def _calculate_distance_matrix(self) -> np.ndarray:
    diff = self.cities[:, np.newaxis, :] - self.cities[np.newaxis, :, :]
    dist_matrix = np.linalg.norm(diff, axis=2)
    return dist_matrix


  def initial_state(self) -> np.ndarray:
    return np.random.permutation(self.num_cities)


  def objective_function(self, state: np.ndarray) -> float:
    tour = self.distance_matrix[state[:-1], state[1:]].sum()
    return tour + self.distance_matrix[state[-1], state[0]]


  # 경로에 포함된 도시의 개수가 num_cities와 같고, 중복된 도시가 없는지 확인
  def is_valid(self, state: np.ndarray) -> bool:
    return len(state) == self.num_cities and len(set(state)) == self.num_cities


  def actions(self, state: np.ndarray) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(len(state)) for j in range(i + 1, len(state))]

  def result(self, state: np.ndarray, action: Tuple[int, int]) -> np.ndarray:
    new_state = state.copy()
    new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
    return new_state

  def goal_test(self, state: np.ndarray) -> bool:
    return False

  def step_cost(self, state: np.ndarray, action: Tuple[int, int]) -> float:
    return 1.

  def hash_state(self, state: np.ndarray) -> int:
    return hash(tuple(state))