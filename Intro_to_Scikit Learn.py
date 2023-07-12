import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

x, y = make_regression(n_samples=200, n_features=1, n_informative=1, noise=30)
# n_samples, n_features, n_informative, noise;

modelo = LinearRegression()  # para criar o modelo com os
# dados que foram extraídos do banco de dados;

plt.scatter(x, y)  # para plotar um gráfico;
plt.plot(x, modelo.predict(x), color='red', lineWidth=3)  # para plotar modelo;
plt.show()  # para mostrar o gráfico;


modelo.fit()  # para treinar o modelo;
modelo.predict()  # para prever os dados;
