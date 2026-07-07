import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

X = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]

reg.fit(X, y)




print(reg.predict([[178]]))
plt.scatter(X, y, color='blue')
plt.plot(X, reg.predict(X), color='red', linewidth=4)		
plt.show()
