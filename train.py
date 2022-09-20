import matplotlib as plot
import numpy as np
import tensorflow as tf
import pandas as pd
df = pd.read_csv("/root/coin/data/ADA_USDT_kline.csv")
print(df)

plot(range(df.shape[0]),(df)/2.0)