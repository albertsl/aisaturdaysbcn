import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')

    total_males = 0
    total_females = 0
    survivor_males = 0
    survivor_females = 0

    #Exercise 2: Let's calculate survivors by passenger class
    global class1_passengers
    global class2_passengers
    global class3_passengers
    global class1_survivors
    global class2_survivors
    global class3_survivors

    total_passengers = df['PassengerId'].count()
    class1_passengers = df[df['Pclass'] == 1]['PassengerId'].count()
    class2_passengers = df[df['Pclass'] == 2]['PassengerId'].count()
    class3_passengers = df[df['Pclass'] == 3]['PassengerId'].count()

    class1_survivors = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]['PassengerId'].count()
    class2_survivors = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]['PassengerId'].count()
    class3_survivors = df[(df['Pclass'] == 3) & (df['Survived'] == 1)]['PassengerId'].count()

    #Exercise 2: Let's calculate survivors by age greater than 18
    global adult_passengers
    global kid_passengers
    global adult_survivors
    global kid_survivors

    total_passengers = df['PassengerId'].count()
    adult_passengers = df[df['Age'] > 18]['PassengerId'].count()
    kid_passengers = df[df['Age'] <= 18]['PassengerId'].count()

    adult_survivors = df[(df['Age'] > 18) & (df['Survived'] == 1)]['PassengerId'].count()
    kid_survivors = df[(df['Age'] <= 18) & (df['Survived'] == 1)]['PassengerId'].count()

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
    plt.bar(['adults', 'kids'], [adult_survivors/adult_passengers, kid_survivors/kid_passengers])
    plt.title('Percent of survivors by age')
    plt.show()

if __name__ == '__main__':
    main()
    plot_exercise2()
