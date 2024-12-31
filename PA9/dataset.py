import numpy as np
import pandas as pd


class Dataset:
  def __init__(self):
    self.data = None
    self.target = None
    self.feature_names = None
    self.target_name = None
    self.load()

  def load(self):
    # ref: https://www.geeksforgeeks.org/house-price-prediction-using-machine-learning-in-python/
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240905183434/HousePricePrediction.xlsx'
    data = pd.read_excel(url)

    bldg_type_dummies = pd.get_dummies(data['BldgType'][:1460], prefix='BldgType')
    total_bsmt_sf = data['TotalBsmtSF'][:1460].values.astype(np.float64)
    self.data = np.hstack((bldg_type_dummies.values, total_bsmt_sf.reshape(-1, 1)))
    self.target = data['SalePrice'][:1460].values.astype(np.float64) / 1000.0
    self.feature_names = list(bldg_type_dummies.columns) + ['size']
    self.target_name = 'price'
