import tensorflow as tf
import pandas as pd
model = tf.keras.models.load_model('model/change.h5')
model.summary()

def predict(dataset):
    column_names = [ 'CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','CH9','CH10','CH11','SR','AI','C', 'F']
    dataset = pd.DataFrame(dataset, columns=column_names)
    y_test = dataset[['C', 'F']]
    account_indexes=dataset['AI']
    x_test = dataset.drop(['C', 'F','AI'], axis=1)
    mean = tf.reduce_mean(x_test, axis=0)
    std = tf.math.reduce_std(x_test, axis=0)
    x_test = (x_test - mean) / std

    test_predictions = model.predict(x_test).flatten()
    percent_accounts=[]
    for i in range(len(x_test)):
        percent_accounts.append([test_predictions[2*i].item(), account_indexes.loc[i].item(),x_test.loc[i].tolist()[:11]])
    return percent_accounts

def predict_commerce(dataset):
    column_names = [ 'CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','CH9','CH10','CH11','SR','AI']
    dataset = pd.DataFrame(dataset, columns=column_names)
    account_indexes=dataset['AI']
    x_test = dataset.drop(['AI'], axis=1)
    mean = tf.reduce_mean(x_test, axis=0)
    std = tf.math.reduce_std(x_test, axis=0)
    x_test = (x_test - mean) / std

    test_predictions = model.predict(x_test).flatten()
    percent_accounts=[]
    for i in range(len(x_test)):
        percent_accounts.append([test_predictions[2*i].item()>test_predictions[2*i+1].item(), account_indexes.loc[i].item(),x_test.loc[i].tolist()[:11]])
    return percent_accounts