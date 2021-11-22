import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from scipy.interpolate import make_interp_spline
from sklearn.linear_model import Ridge

def f(x):
    return 10*np.sin(x)/x

def smooth_curve(x,y):
    x_new = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y, k=3)(x_new)
    return x_new, y_smooth

def generate_train_data(nb):
    x = [np.random.uniform(-3.0, 10.0) for i in range(nb)]
    x = np.sort(x)
    y = f(x) + np.random.normal(0, 1, nb)
    return x, y

def training(degrees, x, y):
    models = [make_pipeline(PolynomialFeatures(degree), Ridge()) for degree in degrees]
    for model in models:
        model.fit(x, y)
    return models

def show_polynomes(models, degrees, x, y):
    colors = ['green', 'red', 'blue', 'orange', 'brown']
    plt.figure()
    plt.title('Plot all models')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y, color='black', s=50, marker='o', label='Training points')
    plt.axis([-4, 12, -5, 15])
    count = 0
    for degree in degrees:
        y_pred = models[count].predict(x)
        x = x.reshape(-1)
        x,y_pred = smooth_curve(x, y_pred)
        x = x.reshape(-1, 1)
        plt.plot(x, y_pred, color=colors[count], linewidth=3, label="degree %d" % degree)
        count += 1
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    x, y = generate_train_data(15)
    degrees = [1, 3, 6, 9, 12]
    # reshape x
    x = x.reshape(-1, 1)
    show_polynomes(training(degrees, x, y), degrees, x, y)

if __name__ == '__main__':
    main()