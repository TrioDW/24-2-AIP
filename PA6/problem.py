from abc import ABC, abstractmethod
from typing import Any, List, Tuple
import random


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


class NQueensProblem(Problem):
    def __init__(self, n: int):
        self.n = n

    def initial_state(self) -> List[int]:
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    # 예. [2, 4, 1, 3, 5, 0]
    def actions(self, state: List[int]) -> List[Tuple[int, int]]:
        actions = []
        for col in range(self.n): # 0 ~ 5
            for row in range(self.n): # 0 ~ 5
                if state[col] != row:
                    actions.append((col, row))
        return actions
    
    # [(0, 0), (0, 1), (0, 3), (0, 4), (0, 5)
    # (1, 0), (1, 1), (1, 2), (1, 3), (1, 5)
    # (2, 0), (2, 2), (2, 3), (2, 4), (2, 5)
    # (3, 0), (3, 1), (3, 2), (3, 4), (3, 5)
    # (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    # (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
        

    def result(self, state: List[int], action: Tuple[int, int]) -> List[int]:
        # 예. [2, 4, 1, 3, 5, 0]
        # col = 0, row = 0
        col, row = action
        new_state = state.copy()
        new_state[col] = row
        return new_state # [0, 4, 1, 3, 5, 0]

    # 예. [2, 4, 1, 3, 5, 0]
    def goal_test(self, state: List[int]) -> bool:
        return self.objective_function(state) == 0

    def step_cost(self, state: List[int], action: Tuple[int, int]) -> float:
        return 1

    # 예. [2, 4, 1, 3, 5, 0]
    # 가로, 세로, 대각선에 대한 충돌 개수 반환하는 함수
    def objective_function(self, state: List[int]) -> int:
        N = len(state)
        conflicts = 0
        col_counts = {}
        diag1_counts = {}
        diag2_counts = {}
        for row in range(N):
            col = state[row]
            col_counts[col] = col_counts.get(col, 0) + 1
            diag1 = col - row
            diag2 = col + row
            diag1_counts[diag1] = diag1_counts.get(diag1, 0) + 1
            diag2_counts[diag2] = diag2_counts.get(diag2, 0) + 1
        for count in col_counts.values():
            if count > 1:
                conflicts += count * (count - 1) // 2
        for count in diag1_counts.values():
            if count > 1:
                conflicts += count * (count - 1) // 2
        for count in diag2_counts.values():
            if count > 1:
                conflicts += count * (count - 1) // 2
        return conflicts

    def objective_function2(self, state: List[int]) -> int:
        conflicts = 0
        N = len(state)
        for i in range(N):
            for j in range(i + 1, N):
                if state[i] == state[j]:
                    conflicts += 1  # Column conflict
                elif abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1  # Diagonal conflict
        return conflicts

    def hash_state(self, state: List[int]) -> int:
        return hash(tuple(state))

    def is_valid(self, state: List[int]) -> bool:
        return len(state) == self.n and all(0 <= col < self.n for col in state)
