import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x = np.array([[1,2,4,0]]).transpose()
y = np.array([[0.5,1,2,0]]).transpose()

reg = linear_model.LinearRegression()
reg.fit(x,y)

#Predict y value for an x value of 5:
print(reg.predict(5))

#Coefficient of the linear regression
print(reg.coef_)

plt.plot(x,y)
plt.show()
