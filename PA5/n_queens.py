from typing import Tuple, List
from problem import Problem

class NQueensProblem(Problem):
    def __init__(self, n: int, initial_state: Tuple[int, ...] = None):
        self.n = n
        if initial_state is not None:
            self.initial = initial_state
        else:
            self.initial = tuple()

    def initial_state(self) -> Tuple[int, ...]:
        return self.initial

    # Actions는 현재 상태에서 수행할 수 있는 유효한 행동을 반환한다.
    def actions(self, state: Tuple[int, ...]) -> List[int]:
        # 초기 state가 (5, ) 일 경우

        # state는 (5, ) 이고, self.n은 8이므로 len(state)는 1이다.
        if len(state) >= self.n:
            return [] 
        
        valid_actions = []
        # row는 0부터 7까지 반복한다.
        for row in range(self.n):
            # new_state는 (5, 0,), (5, 1,), (5, 2,), (5, 3,), (5, 4,), (5, 6,), (5, 7,)이다.
            new_state = state + (row,)
            # new_state가 유효한지 확인한다.
            if self.is_valid(new_state):
                valid_actions.append(row)
        return valid_actions # [0, 1, 2, 3, 7]

    def hash_state(self, state: Tuple[int, ...]) -> int:
        return hash(state)

    # 호출할 때, 각각 (5, 0,), (5, 1,), (5, 2,), (5, 3,), (5, 4,), (5, 6,), (5, 7,)이 유효한지 확인
    def is_valid(self, state: Tuple[int, ...]) -> bool:
        # current_col은 1이다. (1번째 column의 유효한 값을 찾는 것)
        current_col = len(state) - 1

        # col은 0부터 0까지 반복한다.
        for col in range(current_col): # col == 0, current_col == 1
            # 같은 행에 위치하는지 확인
            if state[col] == state[current_col]:
                return False
            # 대각선에 위치하는지 확인
            if abs(state[col] - state[current_col]) == abs(col - current_col):
                return False
        return True
    
    def result(self, state: Tuple[int, ...], action: int) -> Tuple[int, ...]:
        return state + (action,)

    def goal_test(self, state: Tuple[int, ...]) -> bool:
        return len(state) == self.n and self.is_valid(state)

    def step_cost(self, state: Tuple[int, ...], action: int) -> float:
        return 1