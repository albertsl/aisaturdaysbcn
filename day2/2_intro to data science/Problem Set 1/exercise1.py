import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')

total_males = 0
total_females = 0
survivor_males = 0
survivor_females = 0

for passenger_index, passenger in df.iterrows():
    passenger_id = passenger['PassengerId']
    passenger_survived = passenger['Survived']
    passenger_sex = passenger['Sex']
    if passenger_sex == 'male':
        total_males += 1
        if passenger_survived == 1:
            survivor_males += 1
    if passenger_sex == 'female':
        total_females += 1
        if passenger_survived == 1:
            survivor_females += 1

plt.bar(['male','female'], [total_males, total_females])
plt.show()
plt.bar(['male','female'], [survivor_males, survivor_females])
plt.show()
