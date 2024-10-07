import numpy as np
import matplotlib.pyplot as mpl
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input

def task_a(x_data, y_data):
    fig = mpl.figure(figsize=(10, 5))
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)

    reg = LinearRegression().fit(x_data, y_data)
    # reg_score = reg.score(x_data, y_data) 
    ax.plot(x_data, reg.predict(x_data),color='k')

    mpl.show()

def task_b(x_data, y_data):
    fig = mpl.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)

    poly = PolynomialFeatures(2)
    x_poly = poly.fit_transform(x_data)
    reg = LinearRegression().fit(x_poly, y_data)

    ax.plot(x_data, reg.predict(x_poly),color='k')
    mpl.show()

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
    print(y_pred)
    ax.scatter(x_test, y_pred,color='k')
    mpl.show()


def main():
    x_data = np.linspace(-0.5, 0.5, 200)[:,np.newaxis]
    noise = np.random.normal(0, 0.02, x_data.shape)
    y_data = np.square(x_data) + noise
    # y_data = x_data*2 + noise

    task_a(x_data, y_data)
    task_b(x_data, y_data)
    task_c(x_data, y_data)
    

if __name__ == '__main__':
    main()