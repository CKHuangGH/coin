import matplotlib as plot
import numpy as np
import tensorflow as tf
import pandas as pd
df = pd.read_csv("/root/coin/data/ADA_USDT_kline.csv")
print(df)

plot(range(df.shape[0]),(df)/2.0)

train_data = mid\[:525\]
test_data = mid\[525:\]

scaler = MinMaxScaler()
window_size = 800
scaler.transform(train\_data\[di:di+window\_size,:\])

reshape(-1)
scaler.transform(test_data).reshape(-1)
EMA = gamma\*train\[i\] + (1-gamma)\*EMA
  train\[i\] = EMA
pred.append(np.mean(train\[idx-window_size:idx\]))
mse\_errors.append((std\_avg\[-1\]-train\[pred_idx\])**2)