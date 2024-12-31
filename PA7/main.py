from GradientDescentSolver import GradientDescentSolver
from problem import ConvexFunctionProblem


def main():
    # 5차원 벡터 (x1, x2, x3, x4, x5)
    # 값의 범위 : -10 ~ 10
    dimension, bounds = 5, (-10.0, 10.0)

    problem = ConvexFunctionProblem(dimension, bounds)
    solver = GradientDescentSolver(problem, learning_rate=0.01, tolerance=1e-5)
    solution = solver.solve()

    if problem.goal_test(solution):
        print(f"Solution found!")
    else:
        print("Failed!")

if __name__ == "__main__":
    main()