from abc import ABC, abstractmethod
import numpy as np


class Learning(ABC):
    def __init__(self, optimizer, loss):
        self.optimizer = optimizer
        self.loss = loss

    @abstractmethod
    def fit(self, x, y):
        pass

    @abstractmethod
    def predict(self, x):
        pass


class LinearRegression(Learning):
  def __init__(self, optimizer, loss):
    super().__init__(optimizer, loss)
    self.weights = None
    self.bias = None
    self.loss_history = []

  # 10 epochs, batch size 32
  def fit(self, X, y, epochs=100, batch_size=1):
      # 데이터 크기 설정
      n_samples, n_features = X.shape  # n_samples: 샘플 수, n_features: 각 샘플의 특성 수
      self.weights = np.zeros(n_features)  # 가중치 초기화 (특성 수만큼 0으로 초기화)
      self.bias = np.array(0.0)  # 절편(bias) 초기화 (스칼라 값 0.0으로 설정)

      # 에포크 반복
      for epoch in range(epochs):  # 총 epochs 횟수만큼 학습 반복
          indexes = np.arange(n_samples)  # 데이터 인덱스 생성 (0, 1, ..., n_samples-1)
          np.random.shuffle(indexes)  # 데이터를 랜덤하게 셔플링하여 학습 순서를 변경
          X_shuffled = X[indexes]  # 셔플링된 X 데이터
          y_shuffled = y[indexes]  # 셔플링된 y 데이터

          # 배치 학습 반복
          for start_idx in range(0, n_samples, batch_size):  # 배치 크기 단위로 학습
              X_batch = X_shuffled[start_idx:start_idx + batch_size]  # 현재 배치의 X 데이터
              y_batch = y_shuffled[start_idx:start_idx + batch_size]  # 현재 배치의 y 데이터

              # 예측값 계산
              y_pred = np.dot(X_batch, self.weights) + self.bias  
              # 선형 회귀 모델: y_pred = X_batch * weights + bias

              # 손실 계산
              loss = self.loss.compute(y_batch, y_pred)  
              # 손실 함수(MSE)를 사용해 현재 배치의 손실 계산

              # 손실의 그래디언트 계산
              grad_loss = self.loss.gradient(y_batch, y_pred)  
              # 손실 함수의 그래디언트 계산 (y_true - y_pred)

              # 가중치와 절편의 그래디언트 계산
              grad_weights = np.dot(X_batch.T, grad_loss) / batch_size  # 가중치의 그래디언트
              grad_bias = np.sum(grad_loss) / batch_size  # 절편의 그래디언트

              # 옵티마이저를 사용한 파라미터 업데이트
              self.optimizer.step([grad_weights, grad_bias], [self.weights, self.bias])  # 가중치와 절편 업데이트

      # 학습된 가중치와 절편 반환
      return self.weights, self.bias  # 학습 완료된 가중치와 절편 반환


  def predict(self, X):
    return np.dot(X, self.weights) + self.bias


