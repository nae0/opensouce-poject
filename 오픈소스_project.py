import pandas as pd
data=pd.read_csv('gpascore.csv')

#print(data.isnull().sum())
data=data.dropna()

y데이터=data['admit'].values

x데이터=[]

for i, rows in daata.iterrows():
    x데이터.append([rows['gre'], rows['gpa'], rows['rank']])

print(x데이터)

exit()

import numpy as np
import tensorflow as tf

tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accurancy'])

model.fit(np.array(x데이터), np.array(y데이터), epochs=1000)


#예측
예측값 = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(예측값)