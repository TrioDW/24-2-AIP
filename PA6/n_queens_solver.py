from typing import Any, List
from problem import Problem
from solver import Solver


class HillClimbingSolver(Solver):
    def __init__(self, problem: Problem):
        super().__init__(problem)

    def solve(self) -> Any:
        # 6개 만큼 0~5 사이 값으로 random 초기화 (꼭 모든 값이 다를 필요 없음)
        # 예. [2, 4, 1, 3, 5, 0]
        current_state = self.problem.initial_state() 

        if current_state is None:
            raise ValueError("Initial state cannot be None.")  # 초기 상태 검증
        max_iterations = 10000
        iteration = 0

        while iteration < max_iterations: # 최대 10000번 반복
            iteration += 1

            # 목표 상태인지 확인
            if self.problem.goal_test(current_state): # 예. [2, 4, 1, 3, 5, 0]
                return current_state

            # 이웃 상태 생성
            # [(0, 0), (0, 1), (0, 3), (0, 4), (0, 5)
            # (1, 0), (1, 1), (1, 2), (1, 3), (1, 5)
            # (2, 0), (2, 2), (2, 3), (2, 4), (2, 5)
            # (3, 0), (3, 1), (3, 2), (3, 4), (3, 5)
            # (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
            # (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
            neighbors = self._generate_neighbors(current_state)

            if not neighbors:
                raise ValueError("Neighbors cannot be empty.")  # 이웃 상태 검증

            # 다음 상태 선택
            next_state = self._select_next_state(current_state, neighbors)
            # [0, 4, 1, 3, 5, 0]
            if next_state is None:
                raise ValueError("Next state cannot be None.")  # 다음 상태 검증

            # 더 나은 상태가 없으면 종료
            if self.problem.objective_function(next_state) >= self.problem.objective_function(current_state):
                break

            # 상태 갱신
            current_state = next_state

        return current_state

    # 예. [2, 4, 1, 3, 5, 0]
    def _generate_neighbors(self, current_state: Any) -> List[Any]:
        # [(0, 0), (0, 1), (0, 3), (0, 4), (0, 5)
        # (1, 0), (1, 1), (1, 2), (1, 3), (1, 5)
        # (2, 0), (2, 2), (2, 3), (2, 4), (2, 5)
        # (3, 0), (3, 1), (3, 2), (3, 4), (3, 5)
        # (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
        # (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]

        neighbors = self.problem.actions(current_state)
        if not neighbors:
            raise ValueError("Generated neighbors cannot be empty.")  # 이웃 상태 검증
        return neighbors


    # 예. [2, 4, 1, 3, 5, 0]

    # [(0, 0), (0, 1), (0, 3), (0, 4), (0, 5)
    # (1, 0), (1, 1), (1, 2), (1, 3), (1, 5)
    # (2, 0), (2, 2), (2, 3), (2, 4), (2, 5)
    # (3, 0), (3, 1), (3, 2), (3, 4), (3, 5)
    # (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    # (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
    def _select_next_state(self, current_state: Any, neighbors: List[Any]) -> Any:
        best_state = current_state
        best_score = self.problem.objective_function(current_state)

        for neighbor in neighbors:
            next_state = self.problem.result(current_state, neighbor)
            # [0, 4, 1, 3, 5, 0]
            if next_state is None:
                continue  # 결과 상태가 None이면 건너뜀
            score = self.problem.objective_function(next_state)

            if score < best_score:
                best_state = next_state
                best_score = score

        return best_state


class RandomRestartHillClimbingSolver(HillClimbingSolver):
    def __init__(self, problem: Problem, max_restarts: int = 10):
        super().__init__(problem)
        self.max_restarts = max_restarts

    def solve(self) -> Any:
        best_solution = None # 초기에는 최적 solution 없음
        best_score = float('inf') # 최적 score를 발산하여 초기화

        for restart in range(self.max_restarts): # 최대 10번 restart 가능
            current_solution = super().solve() # HillClimbingSolver.solve() 호출

            if current_solution is None:
                raise ValueError("Current solution cannot be None.")  # 현재 상태 검증

            current_score = self.problem.objective_function(current_solution)

            if current_score < best_score:
                best_solution = current_solution
                best_score = current_score

            if best_score == 0:
                break

        if best_solution is None or not self.problem.goal_test(best_solution):
            raise ValueError("No valid solution was found after all restarts.")

        return best_solution
