from sklearn.datasets import load_digits
import numpy as np

from knn import MyKNNClassifier


def my_train_test_split(X, y, test_size=0.3):
  n_samples = X.shape[0]
  n_test = int(n_samples * test_size)

  test_idx = np.random.choice(n_samples, size=n_test, replace=False)
  train_idx = np.setdiff1d(np.arange(n_samples), test_idx)

  X_train, X_test = X[train_idx], X[test_idx]
  y_train, y_test = y[train_idx], y[test_idx]

  return X_train, X_test, y_train, y_test


def main():
    digits = load_digits()
    X = digits.data
    y = digits.target

    X_train, X_test, y_train, y_test = my_train_test_split(X, y, test_size=0.3)

    knn = MyKNNClassifier(k=3, distance_metric='e')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    #print(f"Accuracy: {accuracy: .2f}")

    knn_man = MyKNNClassifier(k=3, distance_metric='m')
    knn_man.fit(X_train, y_train)
    y_pred_man = knn_man.predict(X_test)
    accuracy_man = np.mean(y_pred == y_pred_man)
    #print(f"Accuracy with Manhattan Distance: {accuracy_man: .2f}")
    if 0.9 < accuracy and 0.9 < accuracy_man:
        print("PASS")


if __name__ == "__main__":
    main()
    