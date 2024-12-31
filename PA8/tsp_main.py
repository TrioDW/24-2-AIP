import numpy as np
from ga import GeneticAlgorithmSolver
from problem import TSPProblem


def main():
    # num_cities = 20
    cities = np.array([[20.60535522, 20.84293376],
             [64.32021196, 11.08504038],
             [39.93133893, 49.51685069],
             [83.44668287, 62.10586129],
             [64.78510925, 68.72064081],
             [90.66830849, 24.91714118],
             [86.12748282, 43.83351608],
             [51.28021465, 89.52235316],
             [57.49547908, 98.64397835],
             [47.88843119, 60.40569776],
             [31.34081421, 72.59323658],
             [33.19649003, 57.06480218],
             [96.8802372 , 76.2976494 ],
             [48.22566586, 88.80821079],
             [54.45506476, 48.17920994],
             [17.46971103, 98.72031603],
             [38.80027993, 71.97153381],
             [37.35400107, 38.54452144],
             [52.2752682, 82.46940108],
             [78.86202405, 57.29693797]])

    print(cities)
    tsp_problem = TSPProblem(cities)

    ga_solver = GeneticAlgorithmSolver(
        problem=tsp_problem,
        population_size=500, # 500개의 랜덤 경로 생성
        generations=500, # 최대 반복 횟수
        crossover_rate=0.999, # 교차 확률
        mutation_rate=0.01 # 변이 확률
    )

    best_solution = ga_solver.solve()

    score = tsp_problem.objective_function(best_solution)
    print(tsp_problem.is_valid(best_solution))
    if tsp_problem.is_valid(best_solution):
        if score < 400:
            print('true')


if __name__ == "__main__":
    main()
