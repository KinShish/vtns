import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import json

with open('../../normolize/old/data_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open('../../normolize/old/data_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)

column_names = [ 'CS', 'P', 'A', 'TA','IC', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']#'T',
dataset_train = pd.DataFrame(dataset_train, columns=column_names)
y_train = dataset_train['IC']
x_train = dataset_train.drop(['IC'],axis=1)
# x_train = dataset_train.drop('TA',axis=1)


dataset_test = pd.DataFrame(dataset_test, columns=column_names)
y_test = dataset_test['IC']
x_test = dataset_test.drop(['IC'],axis=1)


def build_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(x_train.shape[1], )),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = build_model()
model.summary()
# print(y_train)
history = model.fit(x_train, y_train, epochs=100,validation_split=0.1)

print(x_test)
print(y_test)
test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)
# test_predictions = model.predict(x_test).flatten()
# count = 0
# for i in range(len(test_predictions)):
#     if i>20:break
#     print(test_predictions[i]==y_test[i])
    # if test_predictions[i]-y_test[i]>0.1:
    #     print(y_test[i]-test_predictions[i])
    #     count+=1
# print(len(x_test),count)

        # print(test_predictions[i], x_test[i], y_test[i], abs(y_test[i] - test_predictions[i]))

