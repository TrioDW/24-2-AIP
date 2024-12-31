from problem import Problem

class Solver:
    def __init__(self, problem: Problem):
        self.problem = problem

    def breadth_first_search(self):
        # (state, actions, states)
        frontier = list()
        frontier.append((self.problem.initial_state(), [], [self.problem.initial_state()]))
        # [((5, ), [], [(5, )])]
        visited = set()
        visited.add(self.problem.hash_state(self.problem.initial_state()))
        # {hash((5, ))}

        while frontier:
            state, actions, states = frontier.pop(0)
            # (5, ), [], [(5, )]
            
            # actions 함수에 (5, )를 넣으면 [0, 1, 2, 3, 7] 반환
            for action in self.problem.actions(state):

                child = self.problem.result(state, action)
                # child는 (5, 0,)이다.

                if self.problem.hash_state(child) not in visited:
                    all_actions = actions + [action] # [0]
                    all_states = states + [child] # [(5, ), (5, 0,)]

                    if self.problem.goal_test(child):
                        return all_states, all_actions # (5, 0,), False

                    frontier.append((child, all_actions, all_states)) # (5, 0,), [0], [(5, ), (5, 0,)]
                    visited.add(self.problem.hash_state(child))

        return None, None