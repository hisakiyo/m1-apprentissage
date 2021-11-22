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
        # reshape x
        x = x.reshape(-1, 1)
        plt.plot(x, y_pred, color=colors[count], linewidth=2, label="degree %d" % degree)
        count += 1
    plt.grid(True)
    plt.legend()
    plt.show()

def compute_errors(models, degrees, x, y):
    counts = 0
    for model in models:
        prediction = model.predict(x)
        print("Degre: %2.f : " % degrees[counts], "MSE: %.2f" % np.mean((prediction - y)**2))
        counts += 1

def print_r_squared(models, degrees, x, y):
    counts = 0
    for model in models:
        prediction = model.predict(x)
        print("Degre: %2.f : " % degrees[counts], "R2: %.2f" % model.score(x, y))
        counts += 1

def main():
    x, y = generate_train_data(15)
    degrees = [1, 3, 6, 9, 12]
    x = x.reshape(-1, 1)
    models = training(degrees, x, y)
    show_polynomes(models, degrees, x, y)
    # Test data
    x_test, y_test = generate_train_data(50)
    x_test = x_test.reshape(-1, 1)
    show_polynomes(models, degrees, x_test, y_test)
    compute_errors(models, degrees, x_test, y_test)
    print_r_squared(models, degrees, x_test, y_test)
    


if __name__ == '__main__':
    main()