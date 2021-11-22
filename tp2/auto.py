# Import panda
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler

def load_dataframe(filename):
    return pd.read_csv(filename)

def main():
    # Load dataframe
    df = load_dataframe('auto-mpg.data')

    df.drop('name', axis=1, inplace=True)
    X = df.drop('mpg', axis=1)
    y = df['mpg']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X_train, y_train)

    print('Score: ', model.score(X_test, y_test))
    print('MSE: ', mean_absolute_error(y_test, model.predict(X_test)))
    print('MAE: ', mean_squared_error(y_test, model.predict(X_test)))

    print('----------------\nNow with scaler:\n----------------')

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_scale = scaler.transform(X_train)
    X_test_scale = scaler.transform(X_test)

    model.fit(X_train_scale, y_train)
    print('New score with scale: ', model.score(X_test_scale, y_test))
    print('New MSE: ', mean_absolute_error(y_test, model.predict(X_test_scale)))
    print('New MAE: ', mean_squared_error(y_test, model.predict(X_test_scale)))


if __name__ == '__main__':
    main()