from matplotlib import pyplot as plt

from dataset import Dataset
from lr import LinearRegression
from utils import MSE
from utils import SGD


def main():
    dataset = Dataset()
    
    # 예측에 사용할 데이터
    X = dataset.data
    # 정답 데이터
    y = dataset.target

    learning_rate = 1e-6  # Small learning rate to ensure stable training
    optimizer = SGD(lr=learning_rate)
    loss_function = MSE()
    model = LinearRegression(optimizer=optimizer, loss=loss_function)

    epochs = 10
    batch_size = 32  # Adjust batch size for better performance
    model.fit(X, y, epochs=epochs, batch_size=batch_size)

    y_pred_all = model.predict(X)
    final_loss = loss_function.compute(y, y_pred_all)

    if final_loss < 5000:
        print('True')


if __name__ == "__main__":
    main()
