import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([[6], [8], [10], [14], [18]])
y = [7, 9, 13, 17.5, 18]


# Création du modèle
model = LinearRegression()
model.fit(X, y)
print("Residual sum of squares: %.2f" % np.sum((model.predict(X) - y) ** 2))