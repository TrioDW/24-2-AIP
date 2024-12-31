from abc import ABC, abstractmethod
from typing import Any

from problem import Problem


class Solver(ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def solve(self) -> Any:
        pass
