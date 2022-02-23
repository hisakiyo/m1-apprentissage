from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def label_encode(data, cols):
    for col in cols:
        # Transforme un type catégorie en entier
        le = LabelEncoder()
        # On récupère tous les noms de catégories possibles
        unique_values = list(data[col].unique())
        le_fitted = le.fit(unique_values)
        # On liste l'ensemble des valeurs
        values = list(data[col].values)
        # On transforme les catégories en entier
        values_transformed = le.transform(values)
        # On fait le remplacement de la colonne dans le dataframe d'origine
        data[col] = values_transformed

# using MLPClassifier
def main():
    # On importe les données
    data = pd.read_csv('human_resources.csv')
    # On change les types de colonnes
    cols_to_labelize = ['sales', 'salary']
    label_encode(data, cols_to_labelize)
    mlp = MLPClassifier()
    # On récupére la première moitié des données pour train
    train_data = data.iloc[:int(len(data) / 2)]
    # On récupére la deuxième moitié des données pour test
    test_data = data.iloc[int(len(data) / 2):]
    # On récupère les colonnes à prédire
    X = train_data.drop(['left'], axis=1)
    # On récupère les colonnes de référence
    y = train_data['left']
    # On entraine le modèle
    mlp.fit(X, y)
    # On prédit
    y_pred = mlp.predict(X)
    # On calcule le taux de réussite
    success_rate = sum(y_pred == y) / len(y)
    print('Train data: ' + str(success_rate))
    # On utilise test
    X_test = test_data.drop(['left'], axis=1)
    y_test = test_data['left']
    y_pred = mlp.predict(X_test)
    success_rate = sum(y_pred == y_test) / len(y_test)
    print('Test data: ' + str(success_rate))


if __name__ == '__main__':
    main()