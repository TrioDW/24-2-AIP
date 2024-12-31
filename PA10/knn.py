from abc import ABC, abstractmethod  # 추상 클래스를 구현하기 위한 모듈
import numpy as np  # 배열 연산 및 수학 계산을 위한 라이브러리


# 추상 클래스 정의
class Learning(ABC):
    def __init__(self, optimizer, loss):
        self.optimizer = optimizer  # Optimizer (사용되지 않음)
        self.loss = loss  # Loss function (사용되지 않음)

    @abstractmethod
    def fit(self, x, y):
        pass  # 데이터를 학습하는 추상 메서드로, 하위 클래스에서 구현 필요

    @abstractmethod
    def predict(self, x):
        pass  # 입력 데이터를 예측하는 추상 메서드로, 하위 클래스에서 구현 필요


# KNN 알고리즘 구현 클래스
class MyKNNClassifier(Learning):
    def __init__(self, k, distance_metric='e', optimizer=None, loss=None):
        super().__init__(optimizer, loss)  # 부모 클래스 생성자 호출
        self.k = k  # KNN에서 고려할 최근접 이웃의 수
        self.distance_metric = distance_metric  # 거리 척도 ('e': Euclidean, 'm': Manhattan)
        self.training_data = None  # 학습 데이터 저장
        self.training_labels = None  # 학습 데이터의 레이블 저장

    def _calculate_distance(self, point1, point2):
        # 두 점 사이의 거리를 계산하는 메서드
        if self.distance_metric == 'e':  # 유클리드 거리 계산
            return np.sqrt(np.sum((point1 - point2) ** 2))
        elif self.distance_metric == 'm':  # 맨해튼 거리 계산
            return np.sum(np.abs(point1 - point2))
        else:
            raise ValueError("Unsupported distance metric")  # 잘못된 거리 척도가 입력된 경우 예외 발생

    def _find_k_nearest_neighbors(self, query_point):
        # 특정 점(query_point)에서 학습 데이터와의 거리를 계산하고 k개의 최근접 이웃을 반환
        distances = [self._calculate_distance(query_point, train_point) for train_point in self.training_data]
        neighbor_indices = np.argsort(distances)[:self.k]  # 거리 기준으로 정렬 후 k개의 인덱스 선택
        return neighbor_indices  # 최근접 이웃의 인덱스 반환

    def _majority_vote(self, neighbors):
        # 최근접 이웃의 레이블에서 다수결 투표 수행
        labels = self.training_labels[neighbors]  # 이웃의 레이블 가져오기
        return np.argmax(np.bincount(labels))  # 가장 많이 등장한 레이블 반환

    def fit(self, X, y):
        # 학습 데이터를 저장 (KNN은 데이터 저장만 수행)
        self.training_data = X
        self.training_labels = y

    def predict(self, X): # X_test
        # 입력 데이터에 대해 예측 수행
        predictions = []  # 예측 결과를 저장할 리스트
        for point in X:  # 입력 데이터의 각 점에 대해
            neighbors = self._find_k_nearest_neighbors(point)  # k개의 최근접 이웃 찾기
            predictions.append(self._majority_vote(neighbors))  # 다수결 투표로 클래스 결정
        return np.array(predictions)  # 예측 결과를 배열로 반환


# 간단한 테스트용 main 함수
if __name__ == "__main__":
    from sklearn.datasets import load_digits  # 데이터셋 로드용 모듈
    from sklearn.model_selection import train_test_split  # 데이터 분리용 함수

    digits = load_digits()  # 손글씨 숫자 데이터셋 로드
    X = digits.data  # 입력 데이터
    y = digits.target  # 레이블 데이터

    # 데이터를 학습/테스트 세트로 분리 (70% 학습, 30% 테스트)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # KNN 모델 생성 및 학습
    knn = MyKNNClassifier(k=3, distance_metric='e')  # 유클리드 거리 사용
    knn.fit(X_train, y_train)  # 모델 학습

    # 예측 및 정확도 계산
    y_pred = knn.predict(X_test)  # 테스트 데이터에 대한 예측
    accuracy = np.mean(y_pred == y_test)  # 정확도 계산
    print(f"Accuracy (Euclidean): {accuracy:.2f}")  # 유클리드 거리 기준 정확도 출력

    # 맨해튼 거리 기준 KNN 테스트
    knn_manhattan = MyKNNClassifier(k=3, distance_metric='m')  # 맨해튼 거리 사용
    knn_manhattan.fit(X_train, y_train)  # 모델 학습
    y_pred_manhattan = knn_manhattan.predict(X_test)  # 테스트 데이터에 대한 예측
    accuracy_manhattan = np.mean(y_pred_manhattan == y_test)  # 정확도 계산
    print(f"Accuracy (Manhattan): {accuracy_manhattan:.2f}")  # 맨해튼 거리 기준 정확도 출력
