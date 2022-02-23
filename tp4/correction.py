import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder


def analyze(data):
    print(data.shape)
    print(data.info())
    print(data.describe())
    print(data.head())
    print(data['left'].value_counts())


def analyze_good_employees(data):
    averages = data.mean()
    average_last_evaluation = averages['last_evaluation']
    average_project = averages['number_project']
    average_montly_hours = averages['average_montly_hours']
    average_time_spend = averages['time_spend_company']

    good_employees = data[data['last_evaluation'] > average_last_evaluation]
    good_employees = good_employees[good_employees['number_project'] > average_project]
    good_employees = good_employees[good_employees['average_montly_hours'] > average_montly_hours]
    good_employees = good_employees[good_employees['time_spend_company'] > average_time_spend]

    sns.set()
    plt.figure(figsize=(15, 8))
    plt.hist(data['left'])
    print(good_employees.shape)
    sns.heatmap(good_employees.corr(), vmax=0.5, cmap="PiYG")
    plt.title('Correlation matrix')
    plt.show()

    print(good_employees.describe())


def label_encode(data):
    # Transforme un type catégorie en entier
    columns = data.columns.values
    for col in columns:
        le = LabelEncoder()
        # On récupère chaque nom de catégories possibles
        unique_values = list(data[col].unique())
        le_fitted = le.fit(unique_values)
        # On liste l'ensemble des valeurs
        values = list(data[col].values)
        # On transforme les catégories en entier
        values_transformed = le.transform(values)
        # On fait le remplacement de la colonne dans le dataframe d'origine
        data[col] = values_transformed


def splitData(data, test_ratio):
    train, test = train_test_split(data, test_size=test_ratio)
    x_train = train
    y_train = train['left']
    del(train['left'])
    x_test = test
    y_test = test['left']
    del(test['left'])
    return x_train, y_train, x_test, y_test

def create_model(classifier, x, y):
    classifier.fit(x, y)
    return classifier


def display_score(classifier, x_train, y_train, x_test, y_test):
    print("Train score: {}, Test score {}".format(classifier.score(x_train, y_train), classifier.score(x_test, y_test)))
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))


def main():
    data_hr = pd.read_csv('human_resources.csv')
    analyze(data_hr)
    analyze_good_employees(data_hr)
    label_encode(data_hr)
    x_train, y_train, x_test, y_test = splitData(data_hr, 0.3)
    classifier = create_model(MLPClassifier(), x_train, y_train)
    display_score(classifier, x_train, y_train, x_test, y_test)


if __name__ == '__main__':
    main()
