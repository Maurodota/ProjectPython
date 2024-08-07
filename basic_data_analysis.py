# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o conjunto de dados
# Você pode substituir 'data.csv' pelo caminho do seu arquivo de dados
data = pd.read_csv('data.csv')

# Exibindo as primeiras linhas do conjunto de dados
print("Primeiras linhas do conjunto de dados:")
print(data.head())

# Informações sobre o conjunto de dados
print("\nInformações sobre o conjunto de dados:")
print(data.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(data.describe())

# Verificando valores ausentes
print("\nValores ausentes por coluna:")
print(data.isnull().sum())

# Preenchendo valores ausentes (se necessário)
# Aqui, substituímos valores ausentes pela mediana da coluna
data = data.fillna(data.median())

# Análise exploratória dos dados
# Distribuição de uma variável contínua
plt.figure(figsize=(10, 6))
sns.histplot(data['nome_da_coluna'], kde=True)
plt.title('Distribuição de nome_da_coluna')
plt.show()

# Gráfico de dispersão entre duas variáveis
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['coluna_x'], y=data['coluna_y'])
plt.title('Dispersão entre coluna_x e coluna_y')
plt.show()

# Gráfico de barras para uma variável categórica
plt.figure(figsize=(10, 6))
sns.countplot(x=data['nome_da_coluna_categorica'])
plt.title('Contagem de nome_da_coluna_categorica')
plt.show()

# Correlação entre variáveis
plt.figure(figsize=(10, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Salvando as estatísticas descritivas em um arquivo CSV
data.describe().to_csv('estatisticas_descritivas.csv')

# Salvando o conjunto de dados limpo em um novo arquivo CSV
data.to_csv('data_clean.csv', index=False)

print("\nAnálise concluída. Estatísticas descritivas e conjunto de dados limpo salvos em arquivos CSV.")
