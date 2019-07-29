import numpy as np
import pandas as pd

def loadData():
    train = np.loadtxt("./src/train1.csv", delimiter=",",dtype = np.float32, skiprows = 1)
    test = np.loadtxt("./src/test1.csv", delimiter=",", dtype=np.float32, skiprows = 1)

    train_df = pd.DataFrame(train)
    test_df = pd.DataFrame(test)

    x_train = train_df.as_matrix(columns=train_df.columns[1:5])
    y_train = train_df.as_matrix(columns=train_df.columns[5:8])
    x_test = test_df.as_matrix(columns=test_df.columns[1:5])
    y_test = test_df.as_matrix(columns=test_df.columns[5:8])

    return x_train, y_train, x_test, y_test

def learning(x_train, y_train, x_test, y_test):
    import keras
    from keras.layers import Input, Embedding, LSTM, Dense
    from keras.models import Model

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(12, input_shape = (4, ), activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(128, activation='relu'))
    #model.add(keras.layers.Dense(32, activation='relu'))
    # model.add(keras.layers.Dense(8, activation='relu'))
    model.add(keras.layers.Dense(3, activation='sigmoid'))
    model.compile(loss="mse", optimizer='adam')
    model.fit(x_train, y_train, epochs=20)

    y_pred = model.predict(x_test)
    print(y_pred)

if __name__ == '__main__':
    x_train, y_train, x_test, y_test = loadData()
    learning(x_train, y_train, x_test, y_test)