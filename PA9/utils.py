from abc import ABC, abstractmethod
import numpy as np


class Loss(ABC):
    @abstractmethod
    def compute(self, y_true, y_pred):
        pass

    @abstractmethod
    def gradient(self, y_true, y_pred):
        pass


class MSE(Loss):
    def compute(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def gradient(self, y_true, y_pred):
        return -2 * (y_true - y_pred) / len(y_true)


class Optimizer(ABC):
    def __init__(self, lr=0.01):
        self.lr = lr

    @abstractmethod
    def step(self, gradients, parameters):
        pass


class SGD(Optimizer):
    def step(self, gradients, parameters):
        for i in range(len(parameters)):
            parameters[i] -= self.lr * gradients[i]
