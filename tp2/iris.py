# Import panda
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def load_dataframe(filename):
    return pd.read_csv(filename)

def main():
    # Load dataframe
    df = load_dataframe('iris.csv')

    df.drop('Id', axis=1, inplace=True)
    X = df.drop('Species', axis=1)
    y = df['Species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    print('Score:', model.score(X_test, y_test))

    # Matrice de confusion
    print('Matrice de confusion')
    y_pred = model.predict(X_test)
    print(pd.crosstab(y_test, y_pred, rownames=['Vrai'], colnames=['Prédit']))

if __name__ == '__main__':
    main()