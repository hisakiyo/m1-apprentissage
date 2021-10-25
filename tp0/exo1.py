import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6], [8], [10], [14], [18]])
y = [7, 9, 13, 17.5, 18]

# Build chart
plt.figure()
plt.title('Pizza prices plotted against sizes')
plt.xlabel('Sizes in cms')
plt.ylabel('Prices in euros')
# show grid
plt.grid(True)
plt.plot(X, y, 'o')

# show
plt.savefig('pizzas.png')
