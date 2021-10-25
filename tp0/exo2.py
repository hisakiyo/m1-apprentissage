import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[6], [8], [10], [14], [18]])
y = [7, 9, 13, 17.5, 18]

# Création du modèle
model = LinearRegression()
model.fit(X, y)
# Affichage du modèle sur plt
plt.plot(X, y, 'o', label='data')
plt.plot(X, model.predict(X), 'r-', label='prediction')
plt.legend(loc='upper left')
plt.grid(True)
plt.savefig('pizzas.png')

