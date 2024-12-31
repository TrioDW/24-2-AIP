from abc import ABC, abstractmethod
from typing import Any, List, Tuple

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
    def hash_state(self, state: Any) -> int:
        # Generates a unique hash for each state, useful for tracking visited states.
        pass

    @abstractmethod
    def is_valid(self, state: Any) -> bool:
        # Checks if a state is valid according to problem-specific rules.
        pass