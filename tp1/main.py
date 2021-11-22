import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from scipy.interpolate import make_interp_spline
from sklearn.linear_model import Ridge

def generate_data(nb):
    x = np.linspace(-3, 10, nb)
    y = 10*np.sin(x)/x + np.random.normal(0, 1, nb)
    return x, y

def data_without_normal_noise(nb):
    x = np.linspace(-3, 10, nb)
    y = 10*np.sin(x)/x
    return x, y

def smooth_curve(x,y):
    x_new = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y, k=3)(x_new)
    return x_new, y_smooth

val = generate_data(15)
real_data = data_without_normal_noise(15)
plt.plot(val[0], val[1], 'o', label='Training points')
plt.grid(True)

# Modèle de degrès 1
pipeline = make_pipeline(PolynomialFeatures(degree=1), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
X,Y = smooth_curve(val[0], y_pred)
plt.plot(X, Y, 'r-', label='degree 1')
print('1: Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

# Modèle de degrès 3
pipeline = make_pipeline(PolynomialFeatures(degree=3), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
X,Y = smooth_curve(val[0], y_pred)
plt.plot(X, Y, 'b-', label='degree 3')
print('3: Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

# Modèle de degrès 6
pipeline = make_pipeline(PolynomialFeatures(degree=6), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
X,Y = smooth_curve(val[0], y_pred)
plt.plot(X, Y, 'y', label='degree 6')
print('6: Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

# Modèle de degrès 9
pipeline = make_pipeline(PolynomialFeatures(degree=9), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
X,Y = smooth_curve(val[0], y_pred)
plt.plot(X, Y, 'y', label='degree 9')
print('9: Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

# Modèle de degrès 12
pipeline = make_pipeline(PolynomialFeatures(degree=12), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
X,Y = smooth_curve(val[0], y_pred)
plt.plot(X, Y, 'y', label='degree 12')
print('12: Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

# Generalisation de la courbe et affichage
x_test = np.linspace(-3, 10, 15)
y_pred = pipeline.predict(x_test.reshape(-1, 1))
X,Y = smooth_curve(x_test, y_pred)
plt.plot(X, Y, 'g', label='Generalization')

# Residual sum of squares between test data and predicted
print('Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))

plt.legend(loc='best')
plt.savefig('pizzas_pred.png')
plt.show()