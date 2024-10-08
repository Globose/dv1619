import numpy as np
import matplotlib.pyplot as mpl
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Input

def task_a(x_data, y_data):
    fig = mpl.figure(figsize=(10, 5))
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)

    # Regression
    reg = LinearRegression().fit(x_data, y_data)
    
    # RMSQ
    rmsq = root_mean_squared_error(y_data, reg.predict(x_data))
    print("Task A RMSQ =", rmsq)
    print("Task A MSQ =", rmsq**2)

    ax.plot(x_data, reg.predict(x_data),color='k')
    # mpl.show()

def task_b(x_data, y_data):
    fig = mpl.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)

    # Regression
    poly = PolynomialFeatures(2)
    x_poly = poly.fit_transform(x_data)
    reg = LinearRegression().fit(x_poly, y_data)
    
    # RMSQ
    rmsq = root_mean_squared_error(y_data, reg.predict(x_poly))
    print("Task B RMSQ =", rmsq)
    print("Task B MSQ =", rmsq**2)

    ax.plot(x_data, reg.predict(x_poly),color='k')
    # mpl.show()

def task_c(x_data, y_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.2, random_state = 0)
    
    # Create model
    model = Sequential()
    model.add(Input(shape = x_train.shape))
    model.add(Dense(6, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Train model
    model.fit(x_train, y_train, epochs=100, verbose=0)

    # Evaluate model
    loss = model.evaluate(x_test, y_test, verbose=2)
    print("Loss =", loss)
    
    # Paint
    fig = mpl.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)
    y_pred = model.predict(x_test, verbose=0).reshape(-1)
    
    # RMSQ
    rmsq = root_mean_squared_error(y_test, y_pred)
    print("Task c RMSQ =", rmsq)
    print("Task c MSQ =", rmsq**2)

    ax.scatter(x_test, y_pred,color='k')


def main():
    x_data = np.linspace(-0.5, 0.5, 200)[:,np.newaxis]
    noise = np.random.normal(0, 0.02, x_data.shape)
    y_data = np.square(x_data) + noise

    task_a(x_data, y_data)
    task_b(x_data, y_data)
    task_c(x_data, y_data)
    mpl.show()
    

if __name__ == '__main__':
    main()