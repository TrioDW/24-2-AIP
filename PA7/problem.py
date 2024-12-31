from abc import ABC, abstractmethod
from typing import Any, List, Tuple
import random
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

# 5, (-10, 10)
class ConvexFunctionProblem(Problem):
    def __init__(self, n: int = 5, bounds: Tuple[float, float] = (-10.0, 10.0)):
        self.n = n
        self.bounds = bounds

    def initial_state(self) -> np.ndarray:
        # -10 ~ 10 사이의 5개 임의의 값을 가진 np.array 
        # 예) [2.5, 3.7, -9.2, 7.8, -2.0]
        initial_state = np.array([np.random.uniform(self.bounds[0], self.bounds[1]) for _ in range(self.n)])
        return initial_state

    def actions(self, state: np.ndarray) -> List[np.ndarray]:
        return np.zeros_like(state)

    def result(self, state: np.ndarray, action: np.ndarray) -> np.ndarray:
        return state + action

    def goal_test(self, state: np.ndarray, tolerance: float = 1e-5) -> bool:
        return self.objective_function(state) < tolerance

    def step_cost(self, state: Any, action: Any) -> float:
        return 0

    def hash_state(self, state: Any) -> int:
        return hash(tuple(state))

    def is_valid(self, state: np.ndarray) -> bool:
        return true

    def objective_function(self, state: np.ndarray) -> float:
        return ((state[0] - 2) ** 2 + 5 * (state[1] - 5) ** 2 +
                8 * (state[2] + 8) ** 2 + 3 * (state[3] + 1) ** 2 +
                6 * (state[4] - 7) ** 2)

    def gradient(self, state: np.ndarray) -> np.ndarray:
        """Symbolic gradient of the objective function."""
        grad = np.zeros_like(state)
        grad[0] = 2 * (state[0] - 2)
        grad[1] = 10 * (state[1] - 5)
        grad[2] = 16 * (state[2] + 8)
        grad[3] = 6 * (state[3] + 1)
        grad[4] = 12 * (state[4] - 7)
        return grad
