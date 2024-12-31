from typing import List

from n_queens_solver import RandomRestartHillClimbingSolver
from problem import NQueensProblem


def main():
    # test case : 6 10
    # n = 6, max_restarts = 10
    n, max_restarts = map(int, input().split())

    problem = NQueensProblem(n) # 6x6 체스판
    solver = RandomRestartHillClimbingSolver(problem, max_restarts)
    solution = solver.solve() # RandomRestartHillClimbingSolver.solve()

    if solution is None or not problem.goal_test(solution):
        print("No solution found:", problem.objective_function(solution))

    else:
        print("Solution found:", problem.objective_function(solution))


def print_board(state: List[int], n: int):
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += "X "
        print(line)
    print()


if __name__ == "__main__":
    main()