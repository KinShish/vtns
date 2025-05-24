import matplotlib.pyplot as plt
import numpy as np
import json

with open('data_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open('data_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)

def getXY(dataset,type):
    x=[]
    y=[]
    for account in dataset[type]["Частный"]:
        x.append(account[1:7])
        y.append(account[6])
    return np.array(x),np.array(y)

x_train,y_train = getXY(dataset_train,"commercial")
x_test,y_test = getXY(dataset_test,"commercial")

import pandas as pd

column_names = [ 'CS', 'P', 'A', 'TA','M', 'C']#'T',, 'C'
x_train = pd.DataFrame(x_train, columns=column_names)
x_train = x_train.sort_values(by='C')

x_train.plot.scatter(x="M",
                         y="C",
                         alpha=0.5);
# c_column = x_train["C"]
# c_column.plot(kind="hist")
plt.show()