import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\User\Desktop\Ciência de Dados - ADA\Módulo 5\Projeto Módulo 5\winequality-red.csv'

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






