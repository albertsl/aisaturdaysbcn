import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')

    total_males = 0
    total_females = 0
    survivor_males = 0
    survivor_females = 0

    total_passengers = df['PassengerId'].count()
    class1_passengers = df[df['Pclass'] == 1].count()
    class2_passengers = df[df['Pclass'] == 2].count()
    class3_passengers = df[df['Pclass'] == 3].count()

    class1_survivors = df[df['Pclass'] == 1 and df['Survived'] == 1].count()
    class2_survivors = df[df['Pclass'] == 2 and df['Survived'] == 1].count()
    class3_survivors = df[df['Pclass'] == 3 and df['Survived'] == 1].count()

    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        passenger_survived = passenger['Survived']
        passenger_sex = passenger['Sex']
        passenger_class = passenger['Pclass']
        passenger_age = passenger['Age']
        if passenger_sex == 'male':
            total_males += 1
            if passenger_survived == 1:
                survivor_males += 1
        if passenger_sex == 'female':
            total_females += 1
            if passenger_survived == 1:
                survivor_females += 1

def plot_exercise1():
    plt.bar(['male','female'], [total_males, total_females])
    plt.title('Total male / female')
    plt.show()
    plt.bar(['male','female'], [survivor_males, survivor_females])
    plt.title('Total survivors male / female')
    plt.show()
    plt.bar(['male','female'], [survivor_males/total_males, survivor_females/total_females])
    plt.title('Percent survivors male / female')
    plt.show()

def plot_exercise2():
    plt.bar(['class 1', 'class 2', 'class 3'], [class1_survivors/class1_passengers, class2_survivors/class2_passengers, class3_survivors/class3_passengers])
    plt.title('Percent of survivors by class')
    plt.show()

if __name__ == '__main__':
    main()
    plot_exercise2()
