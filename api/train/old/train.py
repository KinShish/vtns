import tensorflow as tf
from tensorflow import keras


import numpy as np
import json

with open('../../normolize/old/data_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open('../../normolize/old/data_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)

def getXY(dataset,type):
    x=[]
    y=[]
    for account in dataset[type]["Частный"]:
        x.append(account[1:6])
        y.append(account[6])
    return np.array(x),np.array(y)

x_train,y_train = getXY(dataset_train,"commercial")
x_test,y_test = getXY(dataset_test,"commercial")

import pandas as pd

column_names = [ 'CS', 'P', 'A', 'TA','M']#'T',, 'C'
x_train = pd.DataFrame(x_train, columns=column_names)
# x_train = x_train.sort_values(by='C')
# c_column = x_train["C"]
# c_column.plot(kind="hist")
# plt.show()
# y_train = x_train.pop('C')/
# print(x_train)
def build_model():
    model = keras.Sequential([
        keras.layers.Dense(
          64,activation='elu',
          input_shape=(x_train.shape[-1],)),
        keras.layers.Dense(512,activation='elu'),
        keras.layers.Dense(256, activation='elu'),
        keras.layers.Dense(128, activation='elu'),
        keras.layers.Dense(1),
    ])

    model.compile(optimizer=tf.keras.optimizers.SGD(0.0001),
                  loss='mse',
                  metrics=['mae'])
    return model

model = build_model()
model.summary()
# print(y_train)
history = model.fit(x_train, y_train, epochs=20,validation_split=0.2)
#
test_predictions = model.predict(x_test).flatten()
count = 0
for i in range(len(test_predictions)):
    if i>20:break
    print(test_predictions[i], x_test[i], y_test[i], abs(y_test[i] - test_predictions[i]))
    # if test_predictions[i]-y_test[i]>0.1:
    #     print(y_test[i]-test_predictions[i])
    #     count+=1
# print(len(x_test),count)

        # print(test_predictions[i], x_test[i], y_test[i], abs(y_test[i] - test_predictions[i]))

