import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('home_dataset.csv') 

house_size = data ["HouseSize"].values
house_prices = data ["HousePrice"].values
