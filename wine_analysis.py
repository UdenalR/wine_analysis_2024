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
import numpy as np

# Dados
acidez = sem_outliers_table['volatile acidity']

# Calculando o histograma
plt.figure(figsize=(10, 6))
n, bins, _ = plt.hist(acidez, bins=30, edgecolor='black', alpha=0.75)

# Mapeando os valores de acidez para o colormap
valor_minimo = min(acidez)
valor_maximo = max(acidez)

# Função para mapear valores de acidez para cores
def mapa_cores(valor):
    proporcao = (valor - valor_minimo) / (valor_maximo - valor_minimo)
    return 1 - proporcao  # Invertendo a proporção para obter o efeito desejado

# Adicionando um gradiente de cores com base nos valores de acidez
for i, p in enumerate(plt.gca().patches):
    valor_acidez = (p.get_x() + p.get_width()) / 0.9  # Calculando o valor de acidez para o retângulo
    cor = plt.cm.RdYlBu(mapa_cores(valor_acidez))
    plt.setp(p, 'facecolor', cor)

# Configurações do gráfico
plt.title('Distribuição do Grau de Acidez pela taxa de Acidez Volátil', color='black')
plt.xlabel('Volatile Acidity', color='black')
plt.ylabel('Frequência', color='black')
plt.grid(True, color='none', zorder=0)  # Define a grade atrás do histograma
plt.gca().set_facecolor('white')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['top'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().spines['right'].set_color('black')
plt.xticks(color='black')
plt.yticks(color='black')
plt.show()


# Dados
sulphates = sem_outliers_table['sulphates']
chlorides = sem_outliers_table['chlorides']

# Configurações do gráfico para Sulphates
plt.figure(figsize=(10, 6))

# Calculando o histograma para Sulphates
n_sulphates, bins_sulphates, _ = plt.hist(sulphates, bins=30, edgecolor='black', alpha=0.75)

# Mapeando os valores de sulphates para o colormap
valor_minimo_sulphates = min(sulphates)
valor_maximo_sulphates = max(sulphates)

# Função para mapear valores de sulphates para cores
def mapa_cores_sulphates(valor):
    proporcao = (valor - valor_minimo_sulphates) / (valor_maximo_sulphates - valor_minimo_sulphates)
    return 1 - proporcao  # Invertendo a proporção para obter o efeito desejado

# Adicionando um gradiente de cores com base nos valores de sulphates
for i, p in enumerate(plt.gca().patches):
    valor_sulphates = (p.get_x() + p.get_width()) / 0.9  # Calculando o valor de sulphates para o retângulo
    cor_sulphates = plt.cm.YlGn(mapa_cores_sulphates(valor_sulphates))
    plt.setp(p, 'facecolor', cor_sulphates)

# Configurações do gráfico para Sulphates
plt.title('Distribuição do Grau de Amargor pelo teor de Sulfatos', color='black')
plt.xlabel('Sulphates', color='black')
plt.ylabel('Frequência', color='black')
plt.grid(True, color='none', zorder=0)  # Define a grade atrás do histograma
plt.gca().set_facecolor('white')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['top'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().spines['right'].set_color('black')
plt.xticks(color='black')
plt.yticks(color='black')

# Exibição do gráfico Sulphates
plt.show()

# Configurações do gráfico para Chlorides
plt.figure(figsize=(10, 6))

# Calculando o histograma para Chlorides
n_chlorides, bins_chlorides, _ = plt.hist(chlorides, bins=30, edgecolor='black', alpha=0.75)

# Mapeando os valores de chlorides para o colormap
valor_minimo_chlorides = min(chlorides)
valor_maximo_chlorides = max(chlorides)

# Função para mapear valores de chlorides para cores
def mapa_cores_chlorides(valor):
    proporcao = (valor - valor_minimo_chlorides) / (valor_maximo_chlorides - valor_minimo_chlorides)
    return 1 - proporcao  # Invertendo a proporção para obter o efeito desejado

# Adicionando um gradiente de cores com base nos valores de chlorides
for i, p in enumerate(plt.gca().patches):
    valor_chlorides = (p.get_x() + p.get_width()) / 0.9  # Calculando o valor de chlorides para o retângulo
    cor_chlorides = plt.cm.YlGn(mapa_cores_chlorides(valor_chlorides))
    plt.setp(p, 'facecolor', cor_chlorides)

# Configurações do gráfico para Chlorides
plt.title('Distribuição do Grau de Amargor pelo teor de Cloretos', color='black')
plt.xlabel('Chlorides', color='black')
plt.ylabel('Frequência', color='black')
plt.grid(True, color='none', zorder=0)  # Define a grade atrás do histograma
plt.gca().set_facecolor('white')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['top'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().spines['right'].set_color('black')
plt.xticks(color='black')
plt.yticks(color='black')

# Exibição do gráfico Chlorides
plt.show()