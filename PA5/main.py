from n_queens import NQueensProblem
from solver import Solver

def main():
    n = 8
    initial_state = (5,) # 해당 설정을 통해, 첫 번째 열의 5번째 행에 퀸이 위치하게 됨.
    problem = NQueensProblem(n, initial_state)
    solver = Solver(problem)
    state_sequence, action_sequence = solver.breadth_first_search()
    print_state(state_sequence[-1], n)

def print_state(state, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if col < len(state) and state[col] == row:
                line += "Q "
            else:
                line += "x "
        print(line.rstrip())
    print()

if __name__ == "__main__":
    main()

