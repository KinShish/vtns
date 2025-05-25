import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import json

with open('../normolize/data_train_change.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open('../normolize/data_test_change.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)

column_names = [ 'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','CH9','CH10','CH11','CP','R','P','A','SR','C', 'F']
dataset_train = pd.DataFrame(dataset_train, columns=column_names)
y_train = dataset_train[['C', 'F']]
x_train = dataset_train.drop(['C', 'F','SR'],axis=1)
mean = tf.reduce_mean(x_train, axis=0)
std = tf.math.reduce_std(x_train, axis=0)
x_train = (x_train - mean) / std
print(x_train)


dataset_test = pd.DataFrame(dataset_test, columns=column_names)
y_test = dataset_test[['C', 'F']]
x_test = dataset_test.drop(['C', 'F','SR'],axis=1)
mean = tf.reduce_mean(x_test, axis=0)
std = tf.math.reduce_std(x_test, axis=0)
x_test = (x_test - mean) / std



def build_model():
    model = keras.Sequential([
        keras.layers.Dense(256,input_shape=(x_train.shape[1], ), activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(2, activation='sigmoid')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(0.0001), loss="binary_focal_crossentropy", metrics=['accuracy'])
    return model

model = build_model()
model.summary()
# print(y_train)
history = model.fit(x_train, y_train, epochs=50,validation_split=0.2)

# print(x_test)
# print(y_test)
# test_loss, test_acc = model.evaluate(x_test, y_test)
# print('Test accuracy:', test_acc)

test_predictions = model.predict(x_test).flatten()
# print(test_predictions[0],test_predictions[1],len(test_predictions))


def get_percent(type,y_test):
    count = 0
    all = len(y_test)
    for i in range(len(y_test)):
        if type and y_test.loc[i][type]:
            all-=1
            continue
        # if i>20:break
        if test_predictions[2*i]>=test_predictions[2*i+1]:
            if y_test.loc[i]["C"]:
                count+=1
        else:
            if y_test.loc[i]["F"]:
                count+=1
    print(type,all,count,count/all)
get_percent("C",y_test)
get_percent("F",y_test)
get_percent(0,y_test)
model.save('../model/change_2.h5')

        # print(test_predictions[i], x_test[i], y_test[i], abs(y_test[i] - test_predictions[i]))

