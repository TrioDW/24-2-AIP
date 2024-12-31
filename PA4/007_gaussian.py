import numpy as np

def gaussian_distribution(mean: float, std_dev: float, x: np.ndarray) -> np.ndarray:
    # 정규 분포 공식 대입
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

def identify_anomalies(density_values: np.ndarray, threshold: float) -> np.ndarray:
    # 밀도 값이 임계값보다 작은 인덱스 반환
    return np.where(density_values < threshold)[0]

def main():
    # 난수 생성
    np.random.seed(0)
    # 평균 70, 표준편차 10의 데이터 1000개 생성
    weights = np.random.normal(70, 10, 1000)
    mean = np.mean(weights) # 평균 계산
    std_dev = np.std(weights) # 표준편차 계산
    print(f"Calculated Mean: {mean:.2f}, Calculated Std Dev: {std_dev:.2f}")

    # 이상치 추가
    anomalies = np.array([mean + 3.0 * std_dev, mean - 4.1 * std_dev, mean + 5.0 * std_dev])
    # Concatenate and shuffle
    weights = np.random.permutation(np.concatenate((weights, anomalies)))

    # 확률 밀도 계산
    density_values = gaussian_distribution(mean, std_dev, weights)

    # Threshold 기반 이상치 탐지
    threshold = gaussian_distribution(mean, std_dev, (mean + 4 * std_dev))
    anomaly_indices = identify_anomalies(density_values, threshold)

    # 결과 출력
    print("Anomaly Detection Results (Weights):")
    print(f"Anomalies detected (density < {threshold:.5f}): {len(anomaly_indices)}")
    for i in anomaly_indices:
        print(f"Anomaly: Weight = {weights[i]:.2f} kg, Density = {density_values[i]:.5f}")

if __name__ == "__main__":
    main()