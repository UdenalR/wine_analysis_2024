import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\User\Desktop\Ciência de Dados - ADA\Módulo 5\Projeto Módulo 5\winequality-red.csv'
caminho_outliers = r'C:\Users\User\Desktop\Ciência de Dados - ADA\Módulo 5\Projeto Módulo 5\outliers.csv'
caminho_sem_outliers = r'C:\Users\User\Desktop\Ciência de Dados - ADA\Módulo 5\Projeto Módulo 5\sem_outliers.csv'


# Carregar o arquivo CSV em um dataframe pandas
dataframe = pd.read_csv(caminho_arquivo)

# Exibir o cabeçalho do dataframe (os nomes das colunas)
print(dataframe.head())

print(dataframe.columns)

print(dataframe.info())

print(dataframe.describe())

print(dataframe.isnull().sum())  

print(dataframe['quality'].unique())

dataframe.columns = dataframe.columns.str.strip()  # Remove espaços em branco no início e no final dos nomes das colunas
dataframe.columns = dataframe.columns.str.lower()  # Converte os nomes das colunas para minúsculas

media_por_coluna = dataframe.mean()

# Printar a média de cada coluna
print("Média de cada coluna:")
print(media_por_coluna)


summary = pd.DataFrame({
    'max': dataframe.max(),
    'min': dataframe.min(),
    'mean': dataframe.mean()
})

# Renomear os índices
summary.index = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol',
    'quality'
]

# Exibir a tabela resumo
print(summary)

# Calcular o IQR para cada coluna numérica
Q1 = dataframe.quantile(0.25)
Q3 = dataframe.quantile(0.75)
IQR = Q3 - Q1

# Definir os limites para identificar outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Remover outliers
sem_outliers = dataframe[~((dataframe < limite_inferior) | (dataframe > limite_superior)).any(axis=1)]

# Exibir o novo shape do dataframe após a remoção de outliers
print("Shape do dataframe original:", dataframe.shape)
print("Shape do dataframe sem outliers:", sem_outliers.shape)

# Identificar outliers
outliers = ((dataframe < limite_inferior) | (dataframe > limite_superior))

# Adicionar uma coluna indicando se cada entrada é um outlier ou não
dataframe['outlier'] = outliers.any(axis=1)

# Filtrar linhas que contêm outliers e salvá-las em um arquivo CSV
outliers_table = dataframe[dataframe['outlier']]
outliers_table.to_csv(caminho_outliers, index=False)

# Filtrar linhas que não contêm outliers e salvá-las em um arquivo CSV
sem_outliers_table = dataframe[~dataframe['outlier']]
sem_outliers_table.to_csv(caminho_sem_outliers, index=False)

# Exibir os nomes dos arquivos e seus caminhos
print("Arquivo de outliers:", caminho_outliers)
print("Arquivo sem outliers:", caminho_sem_outliers)

'''
O parâmetro que representa a acidez no gosto de um vinho é a 'volatile acidity' (acidez volátil).
A 'volatile acidity' se refere à quantidade de ácido acético no vinho, que pode contribuir para uma sensação de acidez ou "azedume" na degustação.
'''

import matplotlib.pyplot as plt

# Gere o gráfico de distribuição de acidez
plt.figure(figsize=(10, 6))
plt.hist(sem_outliers_table['volatile acidity'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição de Acidez')
plt.xlabel('Volatile Acidity')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Gere o histograma da distribuição de acidez
plt.figure(figsize=(10, 6))
plt.hist(sem_outliers_table['volatile acidity'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma da Distribuição de Acidez')
plt.xlabel('Volatile Acidity')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()