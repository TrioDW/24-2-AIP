from typing import Any, List

from problem import Problem
from solver import Solver
import numpy as np

# 5, (-10, 10)인 problem, 
class GradientDescentSolver(Solver):
    def __init__(self, problem: Problem, learning_rate: float = 0.01, tolerance: float = 1e-5):
        super().__init__(problem)
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.max_iterations = 1000

    def solve(self) -> Any:
        # 예) [2.5, 3.7, -9.2, 7.8, -2.0]
        current_state = self.problem.initial_state()

        # 1000번 동안 반복 진행
        for i in range(self.max_iterations):
            # 기울기 계산
            gradient = self._numerical_gradient(current_state)

            # 기울기의 크기(노름)가 허용 오차 이하이면 종료
            if np.linalg.norm(gradient) < self.tolerance:
                return current_state

            # 현재 상태 갱신
            current_state = current_state - self.learning_rate * gradient

        return current_state
    
    
    def _numerical_gradient(self, state: np.ndarray) -> np.ndarray:
        """수치 미분을 사용하여 기울기 계산"""

        # 예) state = [2.5, 3.7, -9.2, 7.8, -2.0]
        epsilon = 1e-8

        # [0, 0, 0, 0, 0]
        gradient = np.zeros_like(state)

        for i in range(len(state)):
            state_plus = state.copy()
            state_minus = state.copy()
            state_plus[i] += epsilon
            state_minus[i] -= epsilon

            # i 번째의 위치의 값만 epsilon 만큼 + 또는 - 한다.
            # 그 두 값을 이용하여 objective function 에서 값을 계산하여, 기울기 값을 계산함.
            gradient[i] = (self.problem.objective_function(state_plus) -
                           self.problem.objective_function(state_minus)) / (2 * epsilon)

        return gradient
    