import pandas as pd


df = pd.DataFrame({})

df.shape()  # (Linhas, Colunas)

df.info()  # para saber os tipos de dados de cada coluna,
# quantidade de memoria;

df.columns()  # para alterar o nome das colunas;

df.isnull()  # para saber se tem valores nulos; pode ser usado com .sum();
# que retorna a quantidade de valores nulos;

df['coluna'].unique()  # para saber os valores unicos;

df['coluna'].value_counts().plot(kind='bar')  # para saber a quantidade de
# vezes que o valor aparece; usando outra lib
# chamada matplotlib para gerar o gráfico;

df.describe()  # para saber as medidas estatísticas de cada coluna;

url = 'linkFictio'
df1 = pd.read_csv(url)  # para ler o arquivo e guardar em DataFrame;

sf = pd.read_csv(url)
sf.head()  # para ver as 5 primeiras linhas;
