import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

with open('data_train.json', 'r', encoding='utf-8') as f:
    dataset_train = json.load(f)
with open('data_test.json', 'r', encoding='utf-8') as f:
    dataset_test = json.load(f)



column_names = [ 'T','CS', 'P', 'A', 'TA','IC', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']#, 'C'
x_train = pd.DataFrame(dataset_train, columns=column_names)
x_train.plot.scatter(x="M1",
                         y="T",
                         alpha=0.5);
# c_column = x_train["C"]
# c_column.plot(kind="hist")
plt.show()