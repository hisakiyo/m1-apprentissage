import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

def generate_data(nb):
    x = np.linspace(-3, 10, nb)
    y = 10*np.sin(x)/x + np.random.normal(0, 1, nb)
    return x, y

val = generate_data(13)
plt.plot(val[0], val[1], 'o', label='Training points')
plt.grid(True)

pipeline = make_pipeline(PolynomialFeatures(degree=1), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
plt.plot(val[0], y_pred, 'r-', label='degree 1')

pipeline = make_pipeline(PolynomialFeatures(degree=3), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
plt.plot(val[0], y_pred, 'b-', label='degree 3')

pipeline = make_pipeline(PolynomialFeatures(degree=6), Ridge())
pipeline.fit(val[0].reshape(-1, 1), val[1])
y_pred = pipeline.predict(val[0].reshape(-1, 1))
plt.plot(val[0], y_pred, 'y', label='degree 6')

plt.legend(loc='upper left')
plt.savefig('pizzas_pred.png')

print('Residual sum of squares: %.2f' % np.sum((y_pred - val[1]) ** 2))